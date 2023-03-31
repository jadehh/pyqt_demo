#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : samplesMain.py
# @Author   : jade
# @Date     : 2023/3/31 14:11
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
class Ui_download(object):
    def setupUi(self, Dialog,title):
        self.title=title
        Dialog.setWindowTitle(title)
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(Dialog.width(), Dialog.height())


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_download()
    ui.setupUi(Dialog,"pyqt_demo")
    Dialog.show()
    sys.exit(app.exec_())