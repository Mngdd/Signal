import sys
import subprocess

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../UI/main_window.ui', self)
        self.setWindowTitle('Signal')
        self.setWindowIcon(QtGui.QIcon('../UI/ico-white.png'))

        self.data = {"RAD": {"COORD": (.0, .0, .0), "E": .0, "DIR": (.0, .0, .0)},
                     "OBJ": {"COORD": (.0, .0, .0), "RADIUS": .0},
                     "REC": {"COORD": (.0, .0, .0), "CE": .0}}
        self.distance = 0
        self.Button.clicked.connect(self.calculate)
        self.ERR_MSG.setVisible(False)

    def calculate(self):
        self.ERR_MSG.setVisible(False)

        self.data = {"RAD": {"COORD": (self.RAD_COORD_X.value(), self.RAD_COORD_Y.value(), self.RAD_COORD_Z.value()),
                             "E": self.RAD_ENERGY.value(),
                             "DIR": (self.RAD_DIR_X.value(), self.RAD_DIR_Y.value(), self.RAD_DIR_Z.value())},
                     "OBJ": {"COORD": (self.OBJ_COORD_X.value(), self.OBJ_COORD_Y.value(), self.OBJ_COORD_Z.value()),
                             "RADIUS": self.OBJ_RADIUS.value()},
                     "REC": {"COORD": (self.REC_COORD_X.value(), self.REC_COORD_Y.value(), self.REC_COORD_Z.value()),
                             "CE": self.REC_CE.value()}}

        cmd_args = ["../Signal.exe", self.data['RAD']['E'], *self.data['RAD']['COORD'],
                    *self.data['RAD']['DIR'], *self.data['OBJ']['COORD'], self.data['OBJ']['RADIUS'],
                    *self.data['REC']['COORD'], self.data['REC']['CE']]

        cmd_args = [str(el) for el in cmd_args]

        res = subprocess.run(cmd_args,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err, errcode = res.stdout.strip().decode(), res.stderr, res.returncode
        print(out, len(err), err, errcode)
        self.distance = out
        if len(err) != 0:
            self.raise_err()
            return
        if self.distance == "-1":
            self.ERR_MSG.setText("No objects found...")
            self.ERR_MSG.setVisible(True)
            self.DIST_NUM.setText("NA")
            return
        self.DIST_NUM.setText(self.distance)

    def raise_err(self):
        self.ERR_MSG.setText("Oops, something went wrong! Please check the entered data...")
        self.ERR_MSG.setVisible(True)
        self.DIST_NUM.setText("NA")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())

# mark down
