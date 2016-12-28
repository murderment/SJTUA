#-*- coding:utf-8 -*-
import json
import sys
import os
from PySide import QtCore, QtGui

INITBUG, DYNAMIC, SCHEDULE, MESSAGE, MEMBER, SETTING, BACK = range(7)


class SettingForm(QtGui.QFrame):
    def __init__(self, parent):
        QtGui.QFrame.__init__(self, parent)
        self.parent = parent
        self.setGeometry(0, 60, 1000, 540)
        t = Setting()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)

        font.setFamily("Song Typeface")
        font.setPointSize(18)
        self.btn1 = QtGui.QPushButton(u"返回", self)
        self.btn1.setFlat(True)
        self.btn1.clicked.connect(self._btn1_cb)
        self.btn1.setGeometry(910, 490, 75, 40)
        self.btn1.setFont(font)

        self.tbtn = QtGui.QToolButton(self)
        icon = QtGui.QIcon("plus.png")
        self.tbtn.setIcon(icon)
        self.tbtn.setIconSize(QtCore.QSize(24, 24))
        self.tbtn.clicked.connect(self._tbtn_cb)
        self.tbtn.move(950, 15)


        font.setPointSize(15)
        self.tips_label = QtGui.QLabel(u"开启时界面:", self)
        self.tips_label.setFont(font)
        self.tips_label.setGeometry(10, 10, 280, 25)

        self.setDYNAMIC = QtGui.QRadioButton("Dynamic", self)
        self.setDYNAMIC.setFont(font)
        self.setDYNAMIC.setGeometry(170, 10, 180, 25)

        self.setMEMBER = QtGui.QRadioButton("Member", self)
        self.setMEMBER.setFont(font)
        self.setMEMBER.setGeometry(300, 10, 180, 25)

        self.setMESSAGE = QtGui.QRadioButton("Message", self)
        self.setMESSAGE.setFont(font)
        self.setMESSAGE.setGeometry(430, 10, 180, 25)
        if self.setMESSAGE.toggled.connect(self._checkbox_cb):
            self.parent.convertState(MESSAGE)
            t.saves("loadstate",MESSAGE)


        self.setSCHEDULE = QtGui.QRadioButton("Schedule", self)
        self.setSCHEDULE.setFont(font)
        self.setSCHEDULE.setGeometry(560, 10, 180, 25)
        self.setSCHEDULE.toggled.connect(self._checkbox_cb)

        if state == True:
            print "DDD"
            self.parent.convertState(SCHEDULE)
            t.saves("loadstate", SCHEDULE)



    def _checkbox_cb(self,state):
        assert QtCore.Qt.Unchecked == 0
        assert QtCore.Qt.Checked == 2
        assert state in (QtCore.Qt.Checked, QtCore.Qt.Unchecked, QtCore.Qt.PartiallyChecked)

        print "state:", state





        """self.tips_label = QtGui.QLabel("When you click the close button should me:", self)
        self.tips_label.setGeometry(40, 40, 280, 15)

        self.minimize_rbtn = QtGui.QRadioButton("&Minimize to system tray", self)
        self.minimize_rbtn.setGeometry(70, 90, 180, 20)

        self.exit_rbtn = QtGui.QRadioButton("&Exit program", self)
        self.exit_rbtn.setGeometry(70, 120, 110, 20)

        self.no_confirm_cbox = QtGui.QCheckBox("&Don't ask me again", self)
        self.no_confirm_cbox.setGeometry(40, 180, 150, 20)"""

        """

        self.minimize_rbtn.setChecked(not self._settings['x_action_is_quit'])
        self.exit_rbtn.setChecked(self._settings['x_action_is_quit'])
        self.no_confirm_cbox.setChecked(not self._settings['confirm'])"""

    def _cbx_currentIndexChanged(self):
        pass

    def _tbtn_cb(self):
        pass

    def _btn1_cb(self):
        self.parent.convertState()


class Setting:
    def __init__(self):
        self.dict = {}
        self.path = "setting.json"
        self.load_settings()

    def save_settings(self):
        with open(self.path, 'w') as f:
            buf = json.dumps(self.dict)
            f.write(buf)

    def load_settings(self):
        with open(self.path) as f:
                c = f.read()
                self.dict = json.loads(c)

    def save(self, key, value):
        self.dict[key] = value

    def saves(self, key, value):
        self.dict[key] = value
        self.save_settings()

    def load(self, key):
        return self.dict[key]


def main():
    t = Setting()
    t.save("color", "red")
    t.saves("font", 18)
    print t.load("font")
    print t.dict

main()