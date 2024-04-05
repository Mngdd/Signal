import matplotlib.figure
import matplotlib.pyplot as plt
from math import pi as math_pi
import numpy as np
import random

import os
import sys
import subprocess

import json
import pathlib

import qdarktheme
from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../UI/main_window.ui', self)
        self.setWindowTitle('Signal')
        self.setWindowIcon(QtGui.QIcon('../UI/ico-white.png'))

        self.data = dict()
        with open(pathlib.Path(__file__).parent.resolve().__str__().replace('\\',
                                                                            '/') + "/STARTUP_INPUT.json") as json_file:
            self.data = json.load(json_file)
        self.push_data_to_fields()
        # self.data = {"RL": {"COORD": (self.RAD_COORD_X.value(), self.RAD_COORD_Y.value(), self.RAD_COORD_Z.value()),
        #                      "E": self.RAD_E.value(),
        #                      "DIR": (self.RAD_DIR_X.value(), self.RAD_DIR_Y.value(), self.RAD_DIR_Z.value()),
        #                      "AMP": self.RAD_AMP.value()},
        #              "OBJ": {"COORD": (self.OBJ_COORD_X.value(), self.OBJ_COORD_Y.value(), self.OBJ_COORD_Z.value()),
        #                      "RADIUS": self.OBJ_RADIUS.value(), "REF_IND": self.OBJ_REF_IND.value(),
        #                      "VEL": (self.OBJ_VEL_X.value(), self.OBJ_VEL_Y.value(), self.OBJ_VEL_Z.value())},
        #              "RL": {"COORD": (self.REC_COORD_X.value(), self.REC_COORD_Y.value(), self.REC_COORD_Z.value()),
        #                      "CE": self.REC_CE.value()},
        #              "DELTA_TIME": self.DELTA_TIME.value()}
        self.distance = 0
        self.velocity = 0
        self.sigma = 0
        self.wave_length = 0  # aka Lambda
        self.L = 0
        self.REAL_distance = 0
        self.dark_now = False
        self.warn_stylesheet = "color: rgb(255, 170, 0)"
        self.Button.clicked.connect(self.calculate)
        stylesheet = """ 
                    QTabBar::tab:selected {background: gray;}
                    QTabWidget>QWidget>QWidget{background: gray;}   
                    """
        # посхалко
        name = random.choices(["Mark down && skufidon", "nekit b == gnomie", "Signal"], weights=(1.5, 0.5, 98))[0]
        self.setWindowTitle(name)

        self.setStyleSheet(stylesheet)
        self.setStyleSheet("""
        QMenuBar {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
            border: 1px solid ;
        }

        QMenuBar::item {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
        }

        QMenuBar::item::selected {
            background-color: rgb(30,30,30);
        }

        QMenu {
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
            border: 1px;
        }

        QMenu::item::selected {
            background-color: rgb(30,30,30);
        }
    """)

        self.json_abs_path = pathlib.Path(__file__).parent.resolve().__str__().replace('\\', '/') + "/input.json"
        self.action_save.triggered.connect(self.save)
        self.action_load.triggered.connect(self.load)
        self.action_export.triggered.connect(self.export)
        self.action_draw_plots.triggered.connect(self.draw_plots)
        self.action_draw_scene.triggered.connect(self.draw_scene)
        self.ERR_MSG.setVisible(False)

        self.figure_plots = matplotlib.pyplot.figure()  # заглушка
        self.figure_scene = matplotlib.pyplot.figure(facecolor="lightgrey")
        self.figure_scene.canvas.manager.set_window_title('Scene view')

    def save(self):
        try:
            with open(self.get_file_save_path('Json file (*.json)', 'input.json')[0], "w") as outfile:
                json.dump(self.data, outfile)
        except Exception as err:
            self.show_err_dialog("ERROR", f"failed to save file: {err}")

    def get_file_save_path(self, file_filter, name):
        return QFileDialog.getSaveFileName(
            parent=self,
            caption='Save input',
            directory=name,
            filter=file_filter,
            initialFilter=file_filter
        )

    def load(self):
        try:
            file_filter = 'Json file (*.json)'
            path = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select a JSON file',
                directory=os.getcwd(),
                filter=file_filter,
                initialFilter=file_filter
            )

            with open(path[0]) as json_file:
                self.data = json.load(json_file)

            self.push_data_to_fields()
        except Exception as err:
            self.show_err_dialog("ERROR", f"failed to load file: {err}")

    def push_data_to_fields(self):
        for key in self.data:
            obj = key
            if type(self.data[key]) == dict:
                sub_obj = obj + '_'
                for sub_key in self.data[key]:
                    if type(self.data[key][sub_key]) != float:
                        for i in range(len(self.data[key][sub_key])):
                            exec(f"self.{sub_obj + sub_key + '_' + 'XYZ'[i]}.setValue({self.data[key][sub_key][i]})")
                    else:
                        exec(f"self.{sub_obj + sub_key}.setValue({self.data[key][sub_key]})")
            else:
                exec(f"self.{obj}.setValue({self.data[key]})")

    def export(self):
        dialog = QInputDialog()
        dialog.setLabelText("Enter the number of measurements:")
        dialog.setInputMode(QInputDialog.InputMode.IntInput)
        btn = dialog.exec()

        if not btn:
            return

        self.call_cpp(self.get_file_save_path('Text file (*.txt)', 'exported.txt')[0], str(dialog.intValue()))

    def closeEvent(self, event):
        plt.close('all')
        event.accept()  # let the window close

    def calculate(self):
        self.ERR_MSG.setVisible(False)

        self.data = {"RL": {"COORD": (self.RL_COORD_X.value(), self.RL_COORD_Y.value(), self.RL_COORD_Z.value()),
                            "E": self.RL_E.value(),
                            "DIR": (self.RL_DIR_X.value(), self.RL_DIR_Y.value(), self.RL_DIR_Z.value()),
                            "AMP": self.RL_AMP.value(), "CE": self.RL_CE.value()},
                     "OBJ": {"COORD": (self.OBJ_COORD_X.value(), self.OBJ_COORD_Y.value(), self.OBJ_COORD_Z.value()),
                             "RADIUS": self.OBJ_RADIUS.value(), "REF_IND": self.OBJ_REF_IND.value(),
                             "VEL": (self.OBJ_VEL_X.value(), self.OBJ_VEL_Y.value(), self.OBJ_VEL_Z.value())},
                     "DELTA_TIME": self.DELTA_TIME.value(),
                     "DISTORTION_PERCENT": self.DISTORTION_PERCENT.value()}

        out, err, errcode = self.call_cpp()

        if len(err) != 0 or str(self.distance) in ("nan", "inf") or str(self.velocity) in ("nan", "inf"):
            self.raise_err()
        elif str(self.distance) == "-1":
            self.ERR_MSG.setStyleSheet(self.warn_stylesheet)
            self.ERR_MSG.setText("No objects found...")
            self.ERR_MSG.setVisible(True)
            self.DIST_NUM.setText("NA")
            self.VEL_NUM.setText("NA")
        else:
            self.DIST_NUM.setText(str(self.distance))
            self.VEL_NUM.setText(str(self.velocity))
        try:
            os.remove(self.json_abs_path)
        except ...:
            ...

    def call_cpp(self, path="", amount=""):
        with open(self.json_abs_path, "w") as outfile:
            json.dump(self.data, outfile)
            print("wrote file at", self.json_abs_path)
        if len(amount) * len(path):
            self.json_abs_path += ' ' + path + ' ' + amount
        res = subprocess.run(f"../Signal.exe {self.json_abs_path}",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err, errcode = res.stdout.strip().decode(), res.stderr, res.returncode
        print(out, len(err), err, errcode)
        if not len(amount) * len(path):
            tmp = [float(i) for i in out.split("$RESULT$")[1:]]
            self.distance, self.velocity, self.sigma, self.wave_length, self.L, self.REAL_distance = tmp
        return out, err, errcode

    def draw_plots(self):
        if "NA" in (self.VEL_NUM.text(), self.DIST_NUM.text()):
            self.show_err_dialog("ERROR", "Unable to draw without correct calculations!")
            return

        plt.close(self.figure_plots)
        self.figure_plots.clear()

        abscissa = [i for i in range(11)]
        koef = ((self.data["RL"]["E"] * self.data["RL"]["AMP"] ** 2) /
                ((4 * math_pi * self.distance) ** 2 * 4 * math_pi * self.L))
        pr_sigma = [koef * self.wave_length ** 2 * i for i in range(11)]
        pr_lambda = [koef * i ** 2 * self.sigma for i in range(11)]

        self.figure_plots, axes = plt.subplots(1, 2, figsize=(12.2, 4.8))
        self.figure_plots.canvas.manager.set_window_title('Plots view')
        axes = axes.flatten()

        axes[0].plot(abscissa, pr_sigma)
        axes[1].plot(abscissa, pr_lambda)

        axes[0].set_title("Pr(sigma)")
        axes[0].set_xlabel('Pr')
        axes[0].set_ylabel('sigma')

        axes[1].set_title("Pr(lambda)")
        axes[1].set_xlabel('Pr')
        axes[1].set_ylabel('lambda')
        self.fig_update_ico()
        self.figure_plots.show()

    def draw_scene(self):
        if "NA" in (self.VEL_NUM.text(), self.DIST_NUM.text()):
            self.show_err_dialog("ERROR", "Unable to draw without correct calculations!")
            return

        self.figure_scene.clear()
        self.fig_update_ico()

        self.figure_scene.set_size_inches(4.8, 4.8)
        ax = self.figure_scene.add_subplot((0, 0.05, 1, 0.90), projection='3d', facecolor="lightgrey")

        # объект, станция, дистанция
        self.REAL_distance = sum([(self.data["OBJ"]["COORD"][i] - self.data["RL"]["COORD"][i]) ** 2
                                  for i in range(3)]) ** 0.5
        list_center = [self.data["OBJ"]["COORD"], self.data["RL"]["COORD"], self.data["RL"]["COORD"]]
        list_radius = [self.data["OBJ"]["RADIUS"], 1, self.REAL_distance]
        list_color_info = [('r', 0.8), ('b', 0.9), ('yellow', 0.2)]
        min_, max_ = float("inf"), 0
        for c, r, draw in zip(list_center, list_radius, list_color_info):
            # draw sphere
            u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:20j]
            x = r * np.cos(u) * np.sin(v)
            y = r * np.sin(u) * np.sin(v)
            z = r * np.cos(v)
            min_ = min(np.amin(x), np.amin(y), np.amin(z), min_)  # lowest number in the array
            max_ = max(np.amax(x), np.amax(y), np.amax(z), max_)  # lowest number in the array
            ax.plot_surface(x - c[0], y - c[1], z - c[2], color=draw[0], alpha=draw[1])

        ax.set_xlim3d(min_, max_)
        ax.set_ylim3d(min_, max_)
        ax.set_zlim3d(min_, max_)
        ax.set_aspect("equal")
        self.figure_scene.show()

    def show_err_dialog(self, title, txt):
        QMessageBox.critical(
            self, title, txt,
            buttons=QMessageBox.StandardButton.Ok,
            defaultButton=QMessageBox.StandardButton.Ok,
        )

    def fig_update_ico(self):
        # funny icon and not that stupid matplotlib icon
        PATH_TO_ICON = pathlib.Path(os.path.dirname(__file__)).parent.__str__() + "\\UI\\rofls.png"
        self.figure_plots.canvas.manager.window.setWindowIcon(QtGui.QIcon(PATH_TO_ICON))
        self.figure_scene.canvas.manager.window.setWindowIcon(QtGui.QIcon(PATH_TO_ICON))

    def raise_err(self):
        plt.close()
        self.ERR_MSG.setStyleSheet(self.warn_stylesheet)
        self.ERR_MSG.setText("Something went wrong! Please check the entered data...")
        self.ERR_MSG.setVisible(True)
        self.DIST_NUM.setText("NA")
        self.VEL_NUM.setText("NA")

    def switch_themes(self):
        ...


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    plt.style.use("ggplot")

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainMenu()

    qdarktheme.setup_theme()
    print(app.style())
    ex.setFixedSize(1280, 580)
    qdarktheme.setup_theme(custom_colors={"primary": "#FFA317"})

    app.setStyle('Fusion')
    app.setPalette(qdarktheme.load_palette())

    ex.show()
    sys.exit(app.exec())

# mark down
