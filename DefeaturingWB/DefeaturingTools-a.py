# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
# ***************************************************************************
# *                                                                         *
# *  This file is a part of the Open Source Design456 Workbench - FreeCAD.  *
# *                                                                         *
# *  Copyright (C) 2022                                                    *
# *                                                                         *
# *                                                                         *
# *  This library is free software; you can redistribute it and/or          *
# *  modify it under the terms of the GNU Lesser General Public             *
# *  License as published by the Free Software Foundation; either           *
# *  version 2 of the License, or (at your option) any later version.       *
# *                                                                         *
# *  This library is distributed in the hope that it will be useful,        *
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU      *
# *  Lesser General Public License for more details.                        *
# *                                                                         *
# *  You should have received a copy of the GNU Lesser General Public       *
# *  License along with this library; if not, If not, see                   *
# *  <http://www.gnu.org/licenses/>.                                        *
# *                                                                         *
# *  Modified and added                                                     *
# *  to Design456 by : Mariwan Jalal   mariwan.jalal@gmail.com              *
# ***************************************************************************


# Form implementation generated from reading ui file 'C:\Users\userC\Documents\GitHub\Defeaturing_WB\DefeaturingTools.ui'
#
# Created: Wed Jul 18 12:50:18 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(260, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons-new/Center-Align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DockWidget.setWindowIcon(icon)
        DockWidget.setToolTip("Defeaturing tools")
        DockWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        DockWidget.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        DockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        DockWidget.setWindowTitle("Defeaturing Tools")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.PB_RHoles = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RHoles.setGeometry(QtCore.QRect(12, 288, 32, 32))
        self.PB_RHoles.setToolTip("remove Hole from Face")
        self.PB_RHoles.setText("")
        self.PB_RHoles.setObjectName("PB_RHoles")
        self.PB_Edges = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Edges.setGeometry(QtCore.QRect(220, 36, 32, 32))
        self.PB_Edges.setToolTip("add selected Edges to List")
        self.PB_Edges.setText("")
        self.PB_Edges.setObjectName("PB_Edges")
        self.TE_Faces = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.TE_Faces.setGeometry(QtCore.QRect(24, 164, 190, 71))
        self.TE_Faces.setToolTip("List of Face(s)")
        self.TE_Faces.setObjectName("TE_Faces")
        self.checkBox_keep_original = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_keep_original.setGeometry(QtCore.QRect(124, 252, 110, 33))
        self.checkBox_keep_original.setToolTip("keep the original object")
        self.checkBox_keep_original.setText("keep Object")
        self.checkBox_keep_original.setChecked(True)
        self.checkBox_keep_original.setObjectName("checkBox_keep_original")
        self.InfoLabel = QtGui.QLabel(self.dockWidgetContents)
        self.InfoLabel.setGeometry(QtCore.QRect(24, 0, 196, 36))
        self.InfoLabel.setText("Select Edge(s)\n"
"Ctrl+Click")
        self.InfoLabel.setObjectName("InfoLabel")
        self.TE_Edges = QtGui.QPlainTextEdit(self.dockWidgetContents)
        self.TE_Edges.setEnabled(True)
        self.TE_Edges.setGeometry(QtCore.QRect(24, 36, 190, 66))
        self.TE_Edges.setToolTip("List of Edge(s)")
        self.TE_Edges.setPlainText("")
        self.TE_Edges.setObjectName("TE_Edges")
        self.PB_Faces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Faces.setGeometry(QtCore.QRect(220, 164, 32, 32))
        self.PB_Faces.setToolTip("add selected Faces to List")
        self.PB_Faces.setText("")
        self.PB_Faces.setObjectName("PB_Faces")
        self.PB_Edges_Clear = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Edges_Clear.setGeometry(QtCore.QRect(220, 71, 32, 32))
        self.PB_Edges_Clear.setToolTip("clear List")
        self.PB_Edges_Clear.setText("")
        self.PB_Edges_Clear.setObjectName("PB_Edges_Clear")
        self.PB_Faces_Clear = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Faces_Clear.setGeometry(QtCore.QRect(220, 200, 32, 32))
        self.PB_Faces_Clear.setToolTip("clear List")
        self.PB_Faces_Clear.setText("")
        self.PB_Faces_Clear.setObjectName("PB_Faces_Clear")
        self.Edge_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Edge_Nbr.setGeometry(QtCore.QRect(48, 104, 53, 16))
        self.Edge_Nbr.setText("0")
        self.Edge_Nbr.setObjectName("Edge_Nbr")
        self.Face_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Face_Nbr.setGeometry(QtCore.QRect(48, 236, 53, 16))
        self.Face_Nbr.setText("0")
        self.Face_Nbr.setObjectName("Face_Nbr")
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(24, 124, 177, 45))
        self.label.setText("Select Face(s)\n"
"Ctrl+Click")
        self.label.setObjectName("label")
        self.checkBox_Refine = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_Refine.setGeometry(QtCore.QRect(12, 260, 89, 20))
        self.checkBox_Refine.setToolTip("refine the resulting solid\n"
"after the operation ")
        self.checkBox_Refine.setText("refine")
        self.checkBox_Refine.setChecked(False)
        self.checkBox_Refine.setObjectName("checkBox_Refine")
        self.checkBox_keep_faces = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_keep_faces.setGeometry(QtCore.QRect(128, 140, 100, 20))
        self.checkBox_keep_faces.setToolTip("keep construction faces")
        self.checkBox_keep_faces.setText("keep faces")
        self.checkBox_keep_faces.setObjectName("checkBox_keep_faces")
        self.PB_RFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RFaces.setGeometry(QtCore.QRect(68, 288, 32, 32))
        self.PB_RFaces.setToolTip("remove \'in List\' Faces")
        self.PB_RFaces.setText("")
        self.PB_RFaces.setObjectName("PB_RFaces")
        self.PB_AFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_AFaces.setGeometry(QtCore.QRect(124, 288, 32, 32))
        self.PB_AFaces.setToolTip("add Faces from \'in List\' Edges")
        self.PB_AFaces.setText("")
        self.PB_AFaces.setObjectName("PB_AFaces")
        self.PB_makeShell = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeShell.setGeometry(QtCore.QRect(12, 360, 32, 32))
        self.PB_makeShell.setToolTip("make Solid from in list Faces")
        self.PB_makeShell.setText("")
        self.PB_makeShell.setObjectName("PB_makeShell")
        self.PB_makeShell_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeShell_2.setGeometry(QtCore.QRect(68, 360, 32, 32))
        self.PB_makeShell_2.setToolTip("make Solid from the Faces\n"
"of the selected Objects")
        self.PB_makeShell_2.setText("")
        self.PB_makeShell_2.setObjectName("PB_makeShell_2")
        self.PB_check_TypeId = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_check_TypeId.setGeometry(QtCore.QRect(124, 468, 32, 32))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(False)
        self.PB_check_TypeId.setFont(font)
        self.PB_check_TypeId.setToolTip("show/hide TypeId of the Shape")
        self.PB_check_TypeId.setText("")
        self.PB_check_TypeId.setObjectName("PB_check_TypeId")
        self.Obj_Nbr = QtGui.QLabel(self.dockWidgetContents)
        self.Obj_Nbr.setGeometry(QtCore.QRect(164, 104, 53, 16))
        self.Obj_Nbr.setText("0")
        self.Obj_Nbr.setObjectName("Obj_Nbr")
        self.Obj_Nbr_2 = QtGui.QLabel(self.dockWidgetContents)
        self.Obj_Nbr_2.setGeometry(QtCore.QRect(164, 236, 53, 16))
        self.Obj_Nbr_2.setText("0")
        self.Obj_Nbr_2.setObjectName("Obj_Nbr_2")
        self.PB_AEdges = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_AEdges.setGeometry(QtCore.QRect(220, 288, 32, 32))
        self.PB_AEdges.setToolTip("create a copy of the \'in List\' Edges")
        self.PB_AEdges.setText("")
        self.PB_AEdges.setObjectName("PB_AEdges")
        self.PB_showEdgeList = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_showEdgeList.setGeometry(QtCore.QRect(12, 396, 32, 32))
        self.PB_showEdgeList.setToolTip("show \'in List\' Edge(s)")
        self.PB_showEdgeList.setText("")
        self.PB_showEdgeList.setObjectName("PB_showEdgeList")
        self.PB_showFaceList = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_showFaceList.setGeometry(QtCore.QRect(68, 396, 32, 32))
        self.PB_showFaceList.setToolTip("show \'in List\' Face(s)")
        self.PB_showFaceList.setText("")
        self.PB_showFaceList.setObjectName("PB_showFaceList")
        self.PB_Refine = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_Refine.setGeometry(QtCore.QRect(124, 396, 32, 32))
        self.PB_Refine.setToolTip("refine")
        self.PB_Refine.setText("")
        self.PB_Refine.setObjectName("PB_Refine")
        self.PB_RefineParametric = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RefineParametric.setGeometry(QtCore.QRect(220, 396, 32, 32))
        self.PB_RefineParametric.setToolTip("parametric Refine")
        self.PB_RefineParametric.setText("")
        self.PB_RefineParametric.setObjectName("PB_RefineParametric")
        self.PB_CFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_CFaces.setGeometry(QtCore.QRect(12, 324, 32, 32))
        self.PB_CFaces.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_CFaces.setText("")
        self.PB_CFaces.setObjectName("PB_CFaces")
        self.PB_TFace = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_TFace.setGeometry(QtCore.QRect(68, 324, 32, 32))
        self.PB_TFace.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_TFace.setText("")
        self.PB_TFace.setObjectName("PB_TFace")
        self.offset_input = QtGui.QLineEdit(self.dockWidgetContents)
        self.offset_input.setGeometry(QtCore.QRect(128, 328, 73, 22))
        self.offset_input.setToolTip("Face offset to apply")
        self.offset_input.setText("0.0")
        self.offset_input.setObjectName("offset_input")
        self.PB_TEdge = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_TEdge.setGeometry(QtCore.QRect(220, 324, 32, 32))
        self.PB_TEdge.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_TEdge.setText("")
        self.PB_TEdge.setObjectName("PB_TEdge")
        self.PB_close = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_close.setGeometry(QtCore.QRect(-1, -1, 20, 20))
        self.PB_close.setToolTip("add selected Edges to List")
        self.PB_close.setText("")
        self.PB_close.setObjectName("PB_close")
        self.Version = QtGui.QLabel(self.dockWidgetContents)
        self.Version.setGeometry(QtCore.QRect(200, 0, 53, 16))
        self.Version.setText("0")
        self.Version.setObjectName("Version")
        self.PB_left = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_left.setGeometry(QtCore.QRect(-1, 17, 20, 20))
        self.PB_left.setToolTip("dock left")
        self.PB_left.setText("")
        self.PB_left.setObjectName("PB_left")
        self.PB_right = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_right.setGeometry(QtCore.QRect(-1, 34, 20, 20))
        self.PB_right.setToolTip("dock right")
        self.PB_right.setText("")
        self.PB_right.setObjectName("PB_right")
        self.PB_makeEdge = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_makeEdge.setGeometry(QtCore.QRect(12, 468, 32, 32))
        self.PB_makeEdge.setToolTip("make Edge from selected Vertexes")
        self.PB_makeEdge.setText("")
        self.PB_makeEdge.setObjectName("PB_makeEdge")
        self.PB_expSTEP = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_expSTEP.setGeometry(QtCore.QRect(124, 360, 32, 32))
        self.PB_expSTEP.setToolTip("make Solid from the Faces\n"
"of the selected Objects")
        self.PB_expSTEP.setText("")
        self.PB_expSTEP.setObjectName("PB_expSTEP")
        self.PB_PartDefeaturing = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_PartDefeaturing.setEnabled(False)
        self.PB_PartDefeaturing.setGeometry(QtCore.QRect(172, 288, 32, 32))
        self.PB_PartDefeaturing.setToolTip("show \'in List\' Edge(s)")
        self.PB_PartDefeaturing.setText("")
        self.PB_PartDefeaturing.setObjectName("PB_PartDefeaturing")
        self.PB_CleaningFaces = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_CleaningFaces.setGeometry(QtCore.QRect(220, 360, 32, 32))
        self.PB_CleaningFaces.setToolTip("clean Face(s) removing\n"
"holes and merging Outwire")
        self.PB_CleaningFaces.setText("")
        self.PB_CleaningFaces.setObjectName("PB_CleaningFaces")
        self.PB_checkS = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_checkS.setGeometry(QtCore.QRect(12, 432, 32, 32))
        self.PB_checkS.setToolTip("show \'in List\' Edge(s)")
        self.PB_checkS.setText("")
        self.PB_checkS.setObjectName("PB_checkS")
        self.tolerance_value = QtGui.QLineEdit(self.dockWidgetContents)
        self.tolerance_value.setGeometry(QtCore.QRect(128, 436, 73, 22))
        self.tolerance_value.setToolTip("Face offset to apply")
        self.tolerance_value.setText("0.0")
        self.tolerance_value.setObjectName("tolerance_value")
        self.PB_setTol = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_setTol.setGeometry(QtCore.QRect(220, 432, 32, 32))
        self.PB_setTol.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_setTol.setText("")
        self.PB_setTol.setObjectName("PB_setTol")
        self.PB_getTol = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_getTol.setGeometry(QtCore.QRect(68, 432, 32, 32))
        self.PB_getTol.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_getTol.setText("")
        self.PB_getTol.setObjectName("PB_getTol")
        self.PB_sewS = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_sewS.setGeometry(QtCore.QRect(220, 468, 32, 32))
        self.PB_sewS.setToolTip("copy Faces from \'in List\' Edges")
        self.PB_sewS.setText("")
        self.PB_sewS.setObjectName("PB_sewS")
        self.PB_RHhelp = QtGui.QPushButton(self.dockWidgetContents)
        self.PB_RHhelp.setGeometry(QtCore.QRect(172, 468, 32, 32))
        self.PB_RHhelp.setToolTip("Help")
        self.PB_RHhelp.setText("")
        self.PB_RHhelp.setObjectName("PB_RHhelp")
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)
