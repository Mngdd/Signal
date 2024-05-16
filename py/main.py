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
import logging

import qdarktheme
from PyQt6 import uic, QtGui
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QMessageBox, QInputDialog, QWidget, QLabel)
from PIL import Image

from alpha_beta_filter import alpha_beta_filter

RELATIVE_PATH = pathlib.Path(
    os.path.dirname(__file__)).parent.__str__()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../UI/main_window.ui', self)
        self.setWindowIcon(QtGui.QIcon('../UI/ico-white.png'))
        self.setFixedSize(self.size())
        self.subwindows_ico_path = RELATIVE_PATH + "\\UI\\rofls.png"
        # посхалко
        name = random.choices(
            ["Mark skuf", "nekit mikro skuf", "Signal"],
            weights=(10, 10, 80))[0]
        self.setWindowTitle(name)

        # dict - create input variables dictionary and load default values
        self.data = dict()
        with open(RELATIVE_PATH + "\\py\\STARTUP_INPUT.json") as json_file:
            self.data = json.load(json_file)
        self.push_data_to_fields()  # push dict into input fields

        # variables, that will be returned from main.cpp call
        self.distance = self.velocity = self.sigma = self.wave_length = self.L = 0
        self.calculated_coords = (0, 0, 0)

        # 3d sphere coordinates, will be overwritten on each draw_scene() call
        self.moving_object_coords = self.data["OBJ"]["COORD"]

        # 3d plot gif generating
        self.wait_for_video = False
        self.GifWindowPlayer = GifPlayer(self.subwindows_ico_path)
        self.ProgressBar = LoadBar(self.subwindows_ico_path)

        # stylesheets
        self.warn_stylesheet = "color: rgb(255, 170, 0)"

        self.setStyleSheet(
            """
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
            """
        )

        self.json_abs_path = RELATIVE_PATH + "/input.json"

        self.Button.clicked.connect(self.calculate)
        self.action_save.triggered.connect(self.save_file)
        self.action_load.triggered.connect(self.load_file)
        self.action_export.triggered.connect(self.export_results)
        self.action_draw_plots.triggered.connect(self.draw_plots)
        self.action_draw_scene.triggered.connect(self.draw_scene)
        self.action_draw_scene_anim.triggered.connect(
            lambda: self.draw_scene(True))
        self.ERR_MSG.setVisible(False)

        # empty plots
        self.figure_plots = matplotlib.pyplot.figure()
        self.figure_scene = matplotlib.pyplot.figure(facecolor="lightgrey")
        self.figure_scene.canvas.manager.set_window_title('Scene view')

    def save_file(self):
        try:
            with open(
                    self.get_file_save_path(
                        'Json file (*.json)',
                        'input.json')[0],
                    "w"
            ) as outfile:
                json.dump(self.data, outfile)

        except Exception as err:
            self.show_err_dialog("ERROR", f"failed to save file: {err}")
            logger.warning(f"failed to save file: {err}")

    def get_file_save_path(self, file_filter, name):
        return QFileDialog.getSaveFileName(
            parent=self,
            caption='Save input',
            directory=name,
            filter=file_filter,
            initialFilter=file_filter
        )

    def load_file(self):
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
            logger.warning(f"failed to save file: {err}")

    def push_data_to_fields(self):
        for key in self.data:
            # iterate through keys and check is it map or not
            obj = key
            if isinstance(self.data[key], dict):
                sub_obj = obj + '_'  # path-like name for variable in map, its a root part
                for sub_key in self.data[key]:
                    # then iterate through it again and check is it tuple or single value
                    if isinstance(self.data[key][sub_key], float):
                        exec(f"self.{sub_obj + sub_key}.setValue({self.data[key][sub_key]})")
                    else:
                        for i in range(len(self.data[key][sub_key])):
                            # iterate thorugh each coordinate and put it
                            exec(
                                f"self.{sub_obj + sub_key + '_' + 'XYZ'[i]}.setValue({self.data[key][sub_key][i]})"
                            )
            else:  # generate map value if not dict
                exec(f"self.{obj}.setValue({self.data[key]})")

    def export_results(self):
        dialog = QInputDialog()
        dialog.setLabelText("Enter the number of measurements:")
        dialog.setInputMode(QInputDialog.InputMode.IntInput)
        btn = dialog.exec()

        if not btn:
            return

        out, err, errcode = self.call_cpp(
            self.get_file_save_path('Text file (*.txt)', 'exported.txt')[0],
            str(dialog.intValue())
        )
        if len(err) != 0:
            self.raise_err()

    def closeEvent(self, event):
        plt.close('all')
        event.accept()  # let the window close

    def calculate(self):
        # clear previous error info (it will be overwritten)
        self.ERR_MSG.setVisible(False)

        # load data from inputs
        self.data = {"RL": {"COORD": (
            self.RL_COORD_X.value(), self.RL_COORD_Y.value(),
            self.RL_COORD_Z.value()),
            "E": self.RL_E.value(),
            "DIR": (
                self.RL_DIR_X.value(), self.RL_DIR_Y.value(),
                self.RL_DIR_Z.value()),
            "AMP": self.RL_AMP.value(),
            "CE": self.RL_CE.value()},
            "OBJ": {"COORD": (
                self.OBJ_COORD_X.value(), self.OBJ_COORD_Y.value(),
                self.OBJ_COORD_Z.value()),
                "RADIUS": self.OBJ_RADIUS.value(),
                "REF_IND": self.OBJ_REF_IND.value(),
                "VEL": (
                    self.OBJ_VEL_X.value(), self.OBJ_VEL_Y.value(),
                    self.OBJ_VEL_Z.value())},
            "DELTA_TIME": self.DELTA_TIME.value(),
            "DISTORTION_PERCENT": self.DISTORTION_PERCENT.value()}

        # get cpp calculations and catch errors
        out, err, errcode = self.call_cpp()

        # got weird coords / error
        if len(err) != 0 or str(self.distance) in ("nan", "inf") or str(
                self.velocity) in ("nan", "inf"):
            self.raise_err()
        elif str(self.distance) == "-1":  # no objects found
            self.ERR_MSG.setStyleSheet(self.warn_stylesheet)
            self.ERR_MSG.setText("No objects found...")
            self.ERR_MSG.setVisible(True)
            self.DIST_NUM.setText("NA")
            self.VEL_NUM.setText("NA")
        else:  # success -> write calculated values into output fields
            self.DIST_NUM.setText(str(self.distance))
            self.VEL_NUM.setText(str(self.velocity))
            for i in range(3):
                exec(
                    f"self.COORDS_{['X', 'Y', 'Z'][i]}.setText(str(self.calculated_coords[{i}]))"
                )
        try:  # remove tmp json file, when finished
            os.remove(self.json_abs_path)
        except Exception as err:  # its already deleted
            logger.warning(f"failed to remove temporary json file at: {self.json_abs_path}\n"
                           f"error: {err}")

    def call_cpp(self, path="", amount=""):
        # put data into json and save it
        with open(self.json_abs_path, "w") as outfile:
            json.dump(self.data, outfile)
            logger.info("wrote file at " + self.json_abs_path)
        arguments = self.json_abs_path
        if len(amount) * len(path):
            arguments += ' ' + path + ' ' + amount

        res = subprocess.run(f"../Signal.exe {arguments}",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err, errcode = res.stdout.strip().decode(), res.stderr, res.returncode
        logger.info(f"{out=} {err=} {errcode=}")

        if not len(amount) * len(path):
            # split console output, and remove all garbage output from the left
            tmp = [float(i) for i in out.split("$RESULT$")[1:]]

            (self.distance, self.velocity, self.sigma,
             self.wave_length, self.L, *self.calculated_coords) = tmp
            logger.info(self.calculated_coords)
        return out, err, errcode

    def draw_plots(self):
        if "NA" in (self.VEL_NUM.text(), self.DIST_NUM.text()):
            self.show_err_dialog("ERROR",
                                 "Unable to draw without correct calculations!")
            return

        plt.close(self.figure_plots)
        self.figure_plots.clear()

        dist_dt_measurements = 25
        Pr_measurements = 11
        # axis x for Pr(...) plots
        abscissa = [i for i in range(Pr_measurements)]

        # precalculate Pr
        koef = ((self.data["RL"]["E"] * self.data["RL"]["AMP"] ** 2) /
                ((4 * math_pi * self.distance) ** 2 * 4 * math_pi * self.L))

        # calculate Pr dependence from ...
        pr_sigma = [koef * self.wave_length ** 2 * i for i in range(Pr_measurements)]
        pr_lambda = [koef * i ** 2 * self.sigma for i in range(Pr_measurements)]

        # calculate dist(dt)
        deltas = [i for i in range(dist_dt_measurements)]
        distances = []
        delta_original = self.DELTA_TIME.value()  # save and then restore it
        for i in range(len(deltas)):
            self.DELTA_TIME.setValue(delta_original + i)
            self.call_cpp()
            distances.append(self.distance)
        self.DELTA_TIME.setValue(delta_original)

        # add to plot
        self.figure_plots, axes = plt.subplots(1, 3, figsize=(18.3, 4.8))
        self.figure_plots.canvas.manager.set_window_title('Plots view')
        axes = axes.flatten()

        axes[0].plot(abscissa, pr_sigma)
        axes[1].plot(abscissa, pr_lambda)
        axes[2].plot(deltas, distances)

        axes[0].set_title("PowReceived(sigma)")
        axes[0].set_xlabel('PowReceived')
        axes[0].set_ylabel('sigma')

        axes[1].set_title("PowReceived(lambda)")
        axes[1].set_xlabel('PowReceived')
        axes[1].set_ylabel('lambda')

        axes[2].set_title("distance(DeltaTime)")
        axes[2].set_xlabel('DeltaTime')
        axes[2].set_ylabel('distance')

        self.fig_update_ico()
        self.figure_plots.show()

    def draw_scene(self, do_anim=False):
        if "NA" in (self.VEL_NUM.text(), self.DIST_NUM.text()):
            self.show_err_dialog("ERROR",
                                 "Unable to draw without correct calculations!")
            return

        self.figure_scene.clear()
        self.fig_update_ico()

        self.moving_object_coords = self.data["OBJ"]["COORD"]

        self.figure_scene.set_size_inches(4.8, 4.8)
        ax = self.figure_scene.add_subplot(
            (0, 0.05, 1, 0.90),
            projection='3d',
            facecolor="lightgrey"
        )

        self.calculate_spheres(ax)
        if do_anim:
            frames = 30

            self.ProgressBar.show()
            self.ProgressBar.progress_bar.setValue(0)

            gif_maker = DrawGif(frames, ax, self.figure_scene,
                                self.calculate_spheres)
            gif_maker.countChanged.connect(
                lambda val: self.ProgressBar.progress_bar.setValue(val))
            gif_maker.finished.connect(lambda: self.finish_gif())

            gif_maker.start()
            self.wait_for_video = True

            while self.wait_for_video:
                app.processEvents()  # "update" frame
                QThread.msleep(500)
        else:
            self.figure_scene.show()

    def finish_gif(self):
        self.wait_for_video = False
        self.ProgressBar.hide()
        self.ProgressBar.progress_bar.setValue(0)
        self.GifWindowPlayer.play()

    def calculate_spheres(self, ax: plt.Axes) -> None:
        ax.cla()

        # get real dist between objects
        rl_to_obj_vect = Vector(self.data["RL"]["COORD"],
                                self.moving_object_coords)
        real_distance = rl_to_obj_vect.get_size()

        ax.plot(
            [self.data["RL"]["COORD"][0], self.moving_object_coords[0]],
            [self.data["RL"]["COORD"][1], self.moving_object_coords[1]],
            [self.data["RL"]["COORD"][2], self.moving_object_coords[2]]
        )

        list_center = [self.moving_object_coords, self.data["RL"]["COORD"],
                       self.data["RL"]["COORD"]]
        list_radius = [self.data["OBJ"]["RADIUS"], 1, real_distance]
        names = ["object", "RLS", "distance radius"]
        list_color_info = [('r', 0.8), ('b', 0.9), ('yellow', 0.2)]

        # calculate sphere polygons
        min_, max_ = float("inf"), 0
        for name_, c, r, draw in zip(names, list_center, list_radius,
                                     list_color_info):
            # draw sphere.
            u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:20j]
            x = r * np.cos(u) * np.sin(v)
            y = r * np.sin(u) * np.sin(v)
            z = r * np.cos(v)
            min_ = min(np.amin(x), np.amin(y), np.amin(z),
                       min_)  # lowest number in the array
            max_ = max(np.amax(x), np.amax(y), np.amax(z),
                       max_)  # highest number in the array
            ax.plot_surface(c[0] - x, c[1] - y, c[2] - z, color=draw[0],
                            alpha=draw[1], label=name_)

        ax.text(
            self.data["RL"]["COORD"][0], self.data["RL"]["COORD"][1],
            self.data["RL"]["COORD"][2],
            f"dist={round(real_distance, 3)}", size=15,
            zorder=5, zdir=rl_to_obj_vect.get_direction_vect_lst(),
            color="darkorange"
        )

        ax.set_xlim3d(min_, max_)
        ax.set_ylim3d(min_, max_)
        ax.set_zlim3d(min_, max_)
        ax.set_aspect("equal")
        ax.legend()

        vel_abs = sum(i ** 2 for i in self.data["OBJ"]["VEL"]) ** 0.5
        self.moving_object_coords = tuple(
            self.moving_object_coords[i] + self.data["OBJ"]["VEL"][i] / vel_abs
            for i in range(3)
        )

    def show_err_dialog(self, title, txt):
        QMessageBox.critical(
            self, title, txt,
            buttons=QMessageBox.StandardButton.Ok,
            defaultButton=QMessageBox.StandardButton.Ok,
        )

    def fig_update_ico(self):
        # funny icon and not that stupid matplotlib icon
        self.figure_plots.canvas.manager.window.setWindowIcon(
            QtGui.QIcon(self.subwindows_ico_path))
        self.figure_scene.canvas.manager.window.setWindowIcon(
            QtGui.QIcon(self.subwindows_ico_path))

    def raise_err(self):
        plt.close()
        self.ERR_MSG.setStyleSheet(self.warn_stylesheet)
        self.ERR_MSG.setText(
            "Something went wrong! Please check the entered data...")
        self.ERR_MSG.setVisible(True)
        self.DIST_NUM.setText("NA")
        self.VEL_NUM.setText("NA")
        for i in range(3):
            exec(f"self.COORDS_{['X', 'Y', 'Z'][i]}.setText('NA')")
        self.GifWindowPlayer.hide()
        self.ProgressBar.progress_bar.setValue(0)
        self.ProgressBar.hide()

        try:  # remove tmp json file, when finished
            os.remove(self.json_abs_path)
        except Exception as err:  # its already deleted
            logger.warning(f"failed to remove temporary json file at: {self.json_abs_path}\n"
                           f"error: {err}")


class DrawGif(QThread):
    countChanged = pyqtSignal(int)

    def __init__(self, frames: int, ax: plt.Axes, fig: plt.figure,
                 calc: callable):
        super().__init__()
        self.calc = calc
        self.frames = frames
        self.ax = ax
        self.fig = fig

    def run(self) -> None:
        pics = []
        for i in range(self.frames - 1):
            self.calc(self.ax)
            pics.append(fig2img(self.fig))

            self.countChanged.emit(int((i + 1) / self.frames * 100))
        self.countChanged.emit(100)
        pics[0].save(
            "out.gif", save_all=True, append_images=pics, duration=150, loop=0
        )


class LoadBar(QWidget):
    def __init__(self, subwindows_ico_path):
        super().__init__()
        uic.loadUi('../UI/progress_bar.ui', self)
        self.setWindowIcon(QtGui.QIcon(subwindows_ico_path))
        self.setFixedSize(self.size())

    def closeEvent(self, event):
        event.ignore()


class GifPlayer(QWidget):
    def __init__(self, subwindows_ico_path):
        super().__init__()

        self.setWindowTitle("Animated scene")
        self.setGeometry(300, 300, 480, 480)
        self.setWindowIcon(QtGui.QIcon(subwindows_ico_path))

        self.movie = QtGui.QMovie('out.gif')
        self.label = QLabel(self)
        self.label.resize(480, 480)
        self.setFixedSize(self.size())

    def play(self):
        self.show()
        self.movie = QtGui.QMovie('out.gif')
        self.label.setMovie(self.movie)
        logger.info("starting gif")
        self.movie.start()

    def stop(self):
        self.movie.stop()
        self.hide()


class Vector:
    def __init__(self, a, b):
        self.start = a
        self.end = b

    def get_size(self) -> float:
        return sum(
            [(self.end[i] - self.start[i]) ** 2 for i in range(3)]) ** 0.5

    def __truediv__(self, val):
        new_start = [self.start[i] / val for i in range(3)]
        new_end = [self.end[i] / val for i in range(3)]
        return Vector(new_start, new_end)

    def get_vector_lst(self):
        return [self.end[i] - self.start[i] for i in range(3)]

    def get_direction_vect_lst(self):
        return [a / self.get_size() for a in self.get_vector_lst()]


def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    matplotlib.use("Qt5Agg")
    plt.style.use("ggplot")

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MainMenu()

    qdarktheme.setup_theme()
    qdarktheme.setup_theme(custom_colors={"primary": "#FFA317"})

    app.setStyle('Fusion')
    app.setPalette(qdarktheme.load_palette())

    ex.show()
    sys.exit(app.exec())
