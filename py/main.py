import matplotlib.pyplot as plt
import numpy as np
from math import pi as math_pi

import sys
import subprocess

import json
import pathlib

import qdarktheme
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../UI/main_window.ui', self)
        self.setWindowTitle('Signal')
        self.setWindowIcon(QtGui.QIcon('../UI/ico-white.png'))

        self.data = None
        self.distance = 0
        self.velocity = 0
        self.sigma = 0
        self.wave_length = 0  # aka Lambda
        self.L = 0
        self.Button.clicked.connect(self.calculate)
        self.ERR_MSG.setVisible(False)
        stylesheet = """ 
                    QTabBar::tab:selected {background: gray;}
                    QTabWidget>QWidget>QWidget{background: gray;}
                    """
        self.setStyleSheet(stylesheet)
        self.json_abs_path = pathlib.Path(__file__).parent.resolve().__str__().replace('\\', '/') + "/input.json"

    def closeEvent(self, event):
        print("bye")
        plt.close()
        event.accept()  # let the window close

    def calculate(self):
        self.ERR_MSG.setVisible(False)

        self.data = {"RAD": {"COORD": (self.RAD_COORD_X.value(), self.RAD_COORD_Y.value(), self.RAD_COORD_Z.value()),
                             "E": self.RAD_ENERGY.value(),
                             "DIR": (self.RAD_DIR_X.value(), self.RAD_DIR_Y.value(), self.RAD_DIR_Z.value()),
                             "AMP": self.RAD_AMP.value()},
                     "OBJ": {"COORD": (self.OBJ_COORD_X.value(), self.OBJ_COORD_Y.value(), self.OBJ_COORD_Z.value()),
                             "RADIUS": self.OBJ_RADIUS.value(), "REF_IND": self.OBJ_REF.value(),
                             "VEL": (self.OBJ_VEL_X.value(), self.OBJ_VEL_Y.value(), self.OBJ_VEL_Z.value())},
                     "REC": {"COORD": (self.REC_COORD_X.value(), self.REC_COORD_Y.value(), self.REC_COORD_Z.value()),
                             "CE": self.REC_CE.value()},
                     "DELTA_TIME": self.DELTA_TIME.value()}

        # cmd_args = ["../Signal.exe", self.data['RAD']['E'], *self.data['RAD']['COORD'],
        #             *self.data['RAD']['DIR'], *self.data['OBJ']['COORD'], self.data['OBJ']['RADIUS'],
        #             *self.data['REC']['COORD'], self.data['REC']['CE']]

        out, err, errcode = self.call_cpp()

        if len(err) != 0 or str(self.distance) in ("nan", "inf") or str(self.velocity) in ("nan", "inf"):
            self.raise_err()
            return
        if str(self.distance) == "-1":
            self.ERR_MSG.setText("No objects found...")
            self.ERR_MSG.setVisible(True)
            self.DIST_NUM.setText("NA")
            self.VEL_NUM.setText("NA")
            return
        self.DIST_NUM.setText(str(self.distance))
        self.VEL_NUM.setText(str(self.velocity))
        self.draw_plots()

    def call_cpp(self):
        with open(self.json_abs_path, "w") as outfile:
            json.dump(self.data, outfile)
            print("wrote file at", self.json_abs_path)
            # cmd_args = [str(el) for el in cmd_args]

        res = subprocess.run(f"../Signal.exe {self.json_abs_path}",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err, errcode = res.stdout.strip().decode(), res.stderr, res.returncode
        print(out, len(err), err, errcode)
        tmp = [float(i) for i in out.split("$RESULT$")[1:]]
        self.distance, self.velocity, self.sigma, self.wave_length, self.L = tmp
        return out, err, errcode

    def draw_plots(self):
        abscissa = [i for i in range(11)]
        koef = ((self.data["RAD"]["E"] * self.data["RAD"]["AMP"] ** 2) /
                ((4 * math_pi * self.distance) ** 2 * 4 * math_pi * self.L))
        pr_sigma = [koef * self.wave_length ** 2 * i for i in range(11)]
        pr_lambda = [koef * i ** 2 * self.sigma for i in range(11)]

        figure, axes = plt.subplots(1, 2, figsize=(12.2, 4.8))
        axes = axes.flatten()

        axes[0].plot(abscissa, pr_sigma)
        axes[1].plot(abscissa, pr_lambda)

        axes[0].set_title("Pr(sigma)")
        axes[0].set_xlabel('Pr')
        axes[0].set_ylabel('sigma')

        axes[1].set_title("Pr(lambda)")
        axes[1].set_xlabel('Pr')
        axes[1].set_ylabel('lambda')
        plt.show()

    def raise_err(self):
        plt.close()
        self.ERR_MSG.setText("Oops, something went wrong! Please check the entered data...")
        self.ERR_MSG.setVisible(True)
        self.DIST_NUM.setText("NA")
        self.VEL_NUM.setText("NA")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    plt.style.use("ggplot")

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainMenu()
    print(app.style())
    ex.setFixedSize(1200, 655)

    # qdarktheme.setup_theme()
    qdarktheme.setup_theme(custom_colors={"primary": "#FFA317"})
    app.setStyle('Fusion')
    app.setPalette(qdarktheme.load_palette())

    ex.show()
    sys.exit(app.exec())

# mark down