# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design456Pref.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Design456Preferences(object):
    def setupUi(self, Design456Preferences):
        Design456Preferences.setObjectName("Design456Preferences")
        Design456Preferences.resize(800, 600)
        self.tabConfig = QtWidgets.QTabWidget(Design456Preferences)
        self.tabConfig.setGeometry(QtCore.QRect(110, 0, 691, 581))
        self.tabConfig.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Europe))
        self.tabConfig.setObjectName("tabConfig")
        self.tabfirst = QtWidgets.QWidget()
        self.tabfirst.setObjectName("tabfirst")
        self.grpSimplify = QtWidgets.QGroupBox(self.tabfirst)
        self.grpSimplify.setGeometry(QtCore.QRect(0, 0, 671, 221))
        self.grpSimplify.setObjectName("grpSimplify")
        self.chkSimplify = QtWidgets.QCheckBox(self.grpSimplify)
        self.chkSimplify.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.chkSimplify.setObjectName("chkSimplify")
        self.chkDsableGrid = QtWidgets.QCheckBox(self.grpSimplify)
        self.chkDsableGrid.setGeometry(QtCore.QRect(10, 50, 171, 20))
        self.chkDsableGrid.setObjectName("chkDsableGrid")
        self.tabConfig.addTab(self.tabfirst, "")
        self.tabsecond = QtWidgets.QWidget()
        self.tabsecond.setObjectName("tabsecond")
        self.tabConfig.addTab(self.tabsecond, "")
        self.listWidget = QtWidgets.QListWidget(Design456Preferences)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 111, 581))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(Design456Preferences)
        self.tabConfig.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Design456Preferences)

    def retranslateUi(self, Design456Preferences):
        _translate = QtCore.QCoreApplication.translate
        Design456Preferences.setWindowTitle(_translate("Design456Preferences", "Design456Preferences"))
        self.grpSimplify.setTitle(_translate("Design456Preferences", "Object Creation in Design456"))
        self.chkSimplify.setText(_translate("Design456Preferences", "Simplify created objects"))
        self.chkDsableGrid.setText(_translate("Design456Preferences", "Disable Grid"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tabfirst), _translate("Design456Preferences", "General"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tabsecond), _translate("Design456Preferences", "Others"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Design456Preferences", "General"))
        item = self.listWidget.item(1)
        item.setText(_translate("Design456Preferences", "Others"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
