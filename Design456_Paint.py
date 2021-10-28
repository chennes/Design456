# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
# ***************************************************************************
# *                                                                        *
# * This file is a part of the Open Source Design456 Workbench - FreeCAD.  *
# *                                                                        *
# * Copyright (C) 2021                                                     *
# *                                                                        *
# *                                                                        *
# * This library is free software; you can redistribute it and/or          *
# * modify it under the terms of the GNU Lesser General Public             *
# * License as published by the Free Software Foundation; either           *
# * version 2 of the License, or (at your option) any later version.       *
# *                                                                        *
# * This library is distributed in the hope that it will be useful,        *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of         *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU      *
# * Lesser General Public License for more details.                        *
# *                                                                        *
# * You should have received a copy of the GNU Lesser General Public       *
# * License along with this library; if not, If not, see                   *
# * <http://www.gnu.org/licenses/>.                                        *
# *                                                                        *
# * Author : Mariwan Jalal   mariwan.jalal@gmail.com                       *
# **************************************************************************
import os
import sys
import FreeCAD as App
import FreeCADGui as Gui
import Draft as _draft
import Part as _part
import Design456Init
from pivy import coin
import FACE_D as faced
import math as _math
from PySide.QtCore import QT_TRANSLATE_NOOP
from PySide import QtGui, QtCore
import Draft as _draft
from ThreeDWidgets.constant import FR_BRUSHES
import math
from pivy import coin

#TODO . FIXME


class Design456_Paint:

    brushType: FR_BRUSHES = FR_BRUSHES.FR_SQUARE_BRUSH
    mw = None
    dialog = None  # Dialog for the tool
    tab = None  # Tabs
    smartInd = None  # ?
    _mywin = None                           #
    b1 = None                               #
    PaintLBL = None  # Label
    pl = App.Placement()
    pl.Rotation.Q = (0.0, 0.0, 0.0, 1.0)  # Initial position
    # Initial position - will be changed by the mouse
    pl.Base = App.Vector(0.0, 0.0, 0.0)
    AllObjects = []  # Merged shapes
    cmbBrushSize = None  # GUI combobox -brush size
    cmbBrushType = None  # GUI combobox -brush type
    # current created shape (circle, square, triangles,..etc)
    currentObj = None
    view = None  # used for captureing mouse events
    Observer = None  # Used for captureing mouse events
    continuePainting = True
    brushSize = 1  # Brus Size
    resultObj = None  # Extruded shape
    runOnce = False  # Create the merge object once only
    MoveMentDirection = 'A'

    def setSize(self):
        text = self.cmbBrushSize.currentText()
        if text != "":
            self.brushSize = int(text)

    def setTyep(self):
        text = self.cmbBrushSize.currentText()
        if text != "":
            self.brushType = int(text)

    def draw_circle(self):
        s = _draft.make_circle(self.brushSize, self.pl)
        # Convert/ or get Gui object not App object
        App.ActiveDocument.recompute()
        return(Gui.ActiveDocument.getObject(s.Name))

    def draw_Half_circle(self):
        s = _draft.make_circle(
            self.brushSize, self.pl, True,0, endangle=math.radians(180))
        # Convert/ or get Gui object not App object
        App.ActiveDocument.recompute()
        return(Gui.ActiveDocument.getObject(s.Name))

    def appendToList(self):
        print("Append them to the list")
        Dir = self.currentObj.Object.Shape.normalAt(0, 0)
        tempExtrude = self.currentObj.Object.Shape.extrude(Dir)
        newobj = App.ActiveDocument.addObject(
            "Part::Feature", self.currentObj.Object.Name)
        newobj.Shape = tempExtrude
        self.AllObjects.append(newobj)
        if (self.currentObj is not None):
            App.ActiveDocument.removeObject(self.currentObj.Object.Name)
            self.currentObj = None

    def draw_Square(self):
        s = _draft.make_rectangle(self.brushSize, self.brushSize, self.pl)
        # Convert/ or get Gui object not App object
        App.ActiveDocument.recompute()
        return(Gui.ActiveDocument.getObject(s.Name))

    def draw_polygon(self):
        s =_draft.make_polygon(self.brushSize, self.brushSize, self.pl)
        # Convert/ or get Gui object not App object
        App.ActiveDocument.recompute()        
        if (s is None):
            raise ValueError("s must be an object")
        return(Gui.ActiveDocument.getObject(s.Name))

    def draw_Moon(self):
        pass

    def MouseMovement_cb(self, events):
        event = events.getEvent()
        pos = event.getPosition().getValue()
        tempPos = self.view.getPoint(pos[0], pos[1])
        position = App.Vector(tempPos[0], tempPos[1], tempPos[2])
        if self.currentObj is not None:
            if(self.currentObj.Object.Shape.Placement.Base.z == 0):
                position.z = 0
            elif (self.currentObj.Object.Shape.Placement.Base.y == 0):
                position.y = 0
            elif (self.currentObj.Object.Shape.Placement.Base.x == 0):
                position.x = 0
            # All direction when A or decide which direction
            if (self.MoveMentDirection == 'A'):
                self.currentObj.Object.Placement.Base = position
            elif (self.MoveMentDirection == 'X'):
                self.currentObj.Object.Placement.Base.x = position.x
            elif (self.MoveMentDirection == 'Y'):
                self.currentObj.Object.Placement.Base.x = position.x
            elif (self.MoveMentDirection == 'Z'):
                self.currentObj.Object.Placement.Base.x = position.z

            App.ActiveDocument.recompute()
        else:
            print("Warning!! it was None")

    def MouseClick_cb(self, events):
        event = events.getEvent()
        eventState = event.getState()
        getButton = event.getButton()
        if eventState == coin.SoMouseButtonEvent.DOWN and getButton == coin.SoMouseButtonEvent.BUTTON1:
            print("Place callback!!")
            self.appendToList()
            App.ActiveDocument.recompute()
            self.currentObj = None
            self.setSize()
            self.setType()
            self.recreateObject()

    def recreateObject(self):
        #try:
            if(self.currentObj is not None):
                print("remove object - recreate object",
                      self.currentObj.Object.Name)
                App.ActiveDocument.removeObject(self.currentObj.Object.Name)
                self.currentObj = None

            if self.brushType == FR_BRUSHES.FR_CIRCLE_BRUSH:
                self.currentObj = self.draw_circle()
            elif self.brushType == FR_BRUSHES.FR_HALF_CIRCLE_BRUSH:
                self.currentObj = self.draw_Half_circle()
            elif self.brushType == FR_BRUSHES.FR_TRIANGLE_BRUSH:
                self.currentObj = self.draw_polygon()  # Triangle
            elif self.brushType == FR_BRUSHES.FR_SQUARE_BRUSH:
                self.currentObj = self.draw_Square()
            elif (self.brushType == FR_BRUSHES.FR_FOUR_SIDED_BRUSH or
                  self.brushType == FR_BRUSHES.FR_FIVE_SIDED_BRUSH or
                  self.brushType == FR_BRUSHES.FR_SIX_SIDED_BRUSH):
                self.currentObj = self.draw_polygon()
            elif self.brushType == FR_BRUSHES.FR_MOON_BRUSH:
                self.currentObj = self.draw_Moon()
            if (self.resultObj is None):
                print(len(self.AllObjects), "(len(self.AllObjects)")
                if (len(self.AllObjects) > 1):
                    if(self.runOnce == False):
                        self.runOnce = True
                        self.resultObj = App.ActiveDocument.addObject(
                            "Part::MultiFuse", "Paint")
                        self.resultObj.Refine = True
                        self.resultObj.Shapes = self.AllObjects
            else:
                self.resultObj.Shapes = self.AllObjects

        #except Exception as err:
        #    App.Console.PrintError("'recreate Paint Obj' Failed. "
        #                           "{err}\n".format(err=str(err)))
        #    exc_type, exc_obj, exc_tb = sys.exc_info()
        #    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #    print(exc_type, fname, exc_tb.tb_lineno)
        #    return

    def KeyboardEvent(self, events):
        try:
            event = events.getEvent()
            eventState = event.getState()
            if (type(event) == coin.SoKeyboardEvent):
                key = event.getKey()

            if key == coin.SoKeyboardEvent.X and eventState == coin.SoButtonEvent.UP:
                self.MoveMentDirection = 'X'
            elif key == coin.SoKeyboardEvent.Y and eventState == coin.SoButtonEvent.UP:
                self.MoveMentDirection = 'Y'
            elif key == coin.SoKeyboardEvent.Z and eventState == coin.SoButtonEvent.UP:
                self.MoveMentDirection = 'Z'
            else:
                self.MoveMentDirection = 'A'  # All

            if key == coin.SoKeyboardEvent.ESCAPE and eventState == coin.SoButtonEvent.UP:
                self.remove_callbacks()
            self.hide()

        except Exception as err:
            App.Console.PrintError("'Keyboard error' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return

    def Activated(self):
        self.c1 = None
        self.c2 = None
        print(type(self.currentObj))
        try:
            self.getMainWindow()
            self.view = Gui.ActiveDocument.activeView()
            self.setTyep()
            self.setSize()
            self.recreateObject()            # Initial
            if(self.currentObj is None):
                print("what is that")
            App.ActiveDocument.recompute()
            self.callbackMove = self.view.addEventCallbackPivy(
                coin.SoLocation2Event.getClassTypeId(), self.MouseMovement_cb)
            self.callbackClick = self.view.addEventCallbackPivy(
                coin.SoMouseButtonEvent.getClassTypeId(), self.MouseClick_cb)
            self.callbackKey = self.view.addEventCallbackPivy(
                coin.SoKeyboardEvent.getClassTypeId(), self.KeyboardEvent)

        except Exception as err:
            App.Console.PrintError("'PaintCommand' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def remove_callbacks(self):
        self.view.removeEventCallbackPivy(
            coin.SoLocation2Event.getClassTypeId(), self.callbackMove)
        self.view.removeEventCallbackPivy(
            coin.SoMouseButtonEvent.getClassTypeId(), self.callbackClick)
        self.view.removeEventCallbackPivy(
            coin.SoKeyboardEvent.getClassTypeId(), self.callbackKey)
        self.view = None

    def __del__(self):
        self.remove_callbacks()
        self.mw = None
        self.dialog = None
        self.tab = None
        self.smartInd = None
        self._mywin = None
        self.b1 = None
        self.PaintLBL = None
        self.pl = None
        self.AllObjects = []
        self.cmbBrushSize = None
        self.cmbBrushType = None
        self.currentObj = None
        self.view = None
        self.Observer = None
        self.continuePainting = True
        self.brushSize = 1
        self.brushType = 0
        self.resultObj = None

    def BrushChanged_cb(self):
        # App.ActiveDocument.removeObject(self.currentObj.Object.Name)
        self.currentObj = None
        self.setSize()
        self.setTyep()
        self.recreateObject()
        App.ActiveDocument.recompute()

    def getMainWindow(self):

        try:
            toplevel = QtGui.QApplication.topLevelWidgets()
            self.mw = None
            for i in toplevel:
                if i.metaObject().className() == "Gui::MainWindow":
                    self.mw = i
            if self.mw is None:
                raise Exception("No main window found")
            dw = self.mw.findChildren(QtGui.QDockWidget)
            for i in dw:
                if str(i.objectName()) == "Combo View":
                    self.tab = i.findChild(QtGui.QTabWidget)
                elif str(i.objectName()) == "Python Console":
                    self.tab = i.findChild(QtGui.QTabWidget)
            if self.tab is None:
                raise Exception("No tab widget found")

            self.dialog = QtGui.QDialog()
            oldsize = self.tab.count()
            self.tab.addTab(self.dialog, "Paint")
            self.tab.setCurrentWidget(self.dialog)
            self.dialog.resize(200, 450)
            self.dialog.setWindowTitle("Paint")
            self.formLayoutWidget = QtGui.QWidget(self.dialog)
            self.formLayoutWidget.setGeometry(QtCore.QRect(10, 80, 281, 67))
            self.formLayoutWidget.setObjectName("formLayoutWidget")

            la = QtGui.QVBoxLayout(self.dialog)
            e1 = QtGui.QLabel("Paint")
            commentFont = QtGui.QFont("Times", 12, True)
            self.PaintLBL = QtGui.QLabel("Paint Radius=")
            e1.setFont(commentFont)

            self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
            self.formLayout.setContentsMargins(0, 0, 0, 0)
            self.formLayout.setObjectName("formLayout")
            self.lblPaint = QtGui.QLabel(self.formLayoutWidget)
            self.dialog.setObjectName("Pint")
            self.formLayout.setWidget(
                0, QtGui.QFormLayout.LabelRole, self.lblPaint)
            self.cmbBrushType = QtGui.QComboBox(self.formLayoutWidget)
            self.cmbBrushType.setCurrentText("")
            self.cmbBrushType.setObjectName("cmbBrushType")
            self.formLayout.setWidget(
                0, QtGui.QFormLayout.FieldRole, self.cmbBrushType)
            self.cmbBrushSize = QtGui.QComboBox(self.formLayoutWidget)
            self.cmbBrushSize.setCurrentText("")
            self.cmbBrushSize.setObjectName("cmbBrushSize")
            self.formLayout.setWidget(
                1, QtGui.QFormLayout.FieldRole, self.cmbBrushSize)
            self.lblBrushSize = QtGui.QLabel(self.formLayoutWidget)
            self.lblBrushSize.setObjectName("lblBrushSize")
            self.formLayout.setWidget(
                1, QtGui.QFormLayout.LabelRole, self.lblBrushSize)
            self.formLayoutWidget_2 = QtGui.QWidget(self.dialog)
            self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 160, 80))
            self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
            self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
            self.formLayout_2.setContentsMargins(0, 0, 0, 0)
            self.formLayout_2.setObjectName("formLayout_2")
            self.radioAsIs = QtGui.QRadioButton(self.formLayoutWidget_2)
            self.radioAsIs.setObjectName("radioAsIs")
            self.formLayout_2.setWidget(
                0, QtGui.QFormLayout.FieldRole, self.radioAsIs)
            self.radioMerge = QtGui.QRadioButton(self.formLayoutWidget_2)
            self.radioMerge.setObjectName("radioMerge")
            self.formLayout_2.setWidget(
                1, QtGui.QFormLayout.FieldRole, self.radioMerge)

            la.addWidget(self.formLayoutWidget)
            la.addWidget(e1)
            la.addWidget(self.PaintLBL)
            self.okbox = QtGui.QDialogButtonBox(self.dialog)
            self.okbox.setOrientation(QtCore.Qt.Horizontal)
            self.okbox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
            la.addWidget(self.okbox)

            self.cmbBrushType.addItem("Circle")
            self.cmbBrushType.addItem("Half Circle")
            self.cmbBrushType.addItem("Triangle")
            self.cmbBrushType.addItem("Square")
            self.cmbBrushType.addItem("Four Sided")
            self.cmbBrushType.addItem("Five Sided")
            self.cmbBrushType.addItem("Six sided")
            self.cmbBrushType.addItem("Moon")
            for i in range(1, 400):
                self.cmbBrushSize.addItem(str(i))
            self.cmbBrushSize.setCurrentIndex(FR_BRUSHES.FR_SQUARE_BRUSH)
            self.cmbBrushSize.setCurrentIndex(5)
            self.cmbBrushType.setCurrentIndex(0)
            self.cmbBrushSize.currentTextChanged.connect(self.BrushChanged_cb)
            self.cmbBrushSize.currentIndexChanged.connect(self.BrushChanged_cb)
            self.cmbBrushType.currentTextChanged.connect(self.BrushChanged_cb)
            self.cmbBrushType.currentIndexChanged.connect(self.BrushChanged_cb)

            _translate = QtCore.QCoreApplication.translate
            self.dialog.setWindowTitle(_translate("Pain", "Pint"))
            self.lblPaint.setText(_translate("Dialog", "Brush Type"))
            self.cmbBrushType.setToolTip(_translate("Dialog", "Brush Type"))
            self.cmbBrushSize.setToolTip(_translate("Dialog", "Brush Type"))
            self.lblBrushSize.setText(_translate("Dialog", "Brush Size"))
            self.radioAsIs.setText(_translate("Dialog", "As is"))
            self.radioMerge.setText(_translate("Dialog", "Merge"))

            QtCore.QMetaObject.connectSlotsByName(self.dialog)
            QtCore.QObject.connect(self.okbox, QtCore.SIGNAL("accepted()"), self.hide)
            return self.dialog

        except Exception as err:
            App.Console.PrintError("'Design456_Paint' getMainWindwo-Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def hide(self):
        """
        Hide the widgets. Remove also the tab.
        """
        App.ActiveDocument.removeObject(self.currentObj.Object.Name)
        self.currentObj = None
        App.ActiveDocument.recompute()
        self.dialog.hide()
        del self.dialog
        dw = self.mw.findChildren(QtGui.QDockWidget)
        newsize = self.tab.count()  # Todo : Should we do that?
        self.tab.removeTab(newsize-1)  # it ==0,1,2,3 ..etc

        App.ActiveDocument.recompute()
        self.__del__()  # Remove all Paint 3dCOIN widgets

    def GetResources(self):
        return {'Pixmap': Design456Init.ICON_PATH + 'Design456_Paint.svg',
                'MenuText': "Paint",
                'ToolTip': "Draw or Paint"}


Gui.addCommand('Design456_Paint', Design456_Paint())
