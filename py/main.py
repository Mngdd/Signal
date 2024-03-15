import sys
import subprocess
import json
import pathlib
import qdarktheme

from PyQt6 import uic, QtGui
from PyQt6.QtCore import QVariantAnimation
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
        self.Button.clicked.connect(self.calculate)
        self.ERR_MSG.setVisible(False)

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
        global_path = pathlib.Path(__file__).parent.resolve().__str__().replace('\\', '/') + "/input.json"

        with open(global_path, "w") as outfile:
            json.dump(self.data, outfile)
            print("wrote file at", global_path)
        # cmd_args = [str(el) for el in cmd_args]

        res = subprocess.run(f"../Signal.exe {global_path}",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err, errcode = res.stdout.strip().decode(), res.stderr, res.returncode
        print(out, len(err), err, errcode)
        self.distance = out.split("$RESULT$")[1]
        self.velocity = out.split("$RESULT$")[2]
        if len(err) != 0:
            self.raise_err()
            return
        if self.distance == "-1":
            self.ERR_MSG.setText("No objects found...")
            self.ERR_MSG.setVisible(True)
            self.DIST_NUM.setText("NA")
            self.VEL_NUM.setText("NA")
            return
        self.DIST_NUM.setText(self.distance)
        self.VEL_NUM.setText(self.velocity)

def raise_err(self):
        self.ERR_MSG.setText("Oops, something went wrong! Please check the entered data...")
        self.ERR_MSG.setVisible(True)
        self.DIST_NUM.setText("NA")
        self.VEL_NUM.setText("NA")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainMenu()
    print(app.style())

    #qdarktheme.setup_theme()
    qdarktheme.setup_theme(custom_colors={"primary": "#FFA317"})
    app.setStyle('Fusion')
    app.setPalette(qdarktheme.load_palette())

    ex.show()
    sys.exit(app.exec())

# mark down
