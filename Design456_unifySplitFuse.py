# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PySide.QtCore import QT_TRANSLATE_NOOP
from draftobjects.base import DraftObject
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
# * Author : Mario52                                                       *
# * ##Macro_D_Un_Jour_Raccord_2_Objects_By_Its_Faces                       *
# * #https://forum.freecadweb.org/viewtopic.php?f=3&t=56185&p=483304&hilit=slice#p483304
# * #12/03/2021
#                                                                          *
# * select the faces for raccord                                           *
# * Modified and added to Design456 WB by :                                *
# * Author Mariwan Jalal   mariwan.jalal@gmail.com                         *
# **************************************************************************
import os
import sys
import ImportGui
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui, QtCore  # https://www.freecadweb.org/wiki/PySide
import Draft as _draft
import Part as _part
import Design456Init
from pivy import coin
import FACE_D as faced
import math as _math


class Design456_unifySplitFuse1:
    
    def Activated(self):
         
 
        #### Config Begin ####
        switchRemoveConstructionObject = switchRemoveConstructionObject = self.askQuestion()    # if 0= (NO) not removed creation objects 1= (YES) remove objects
        switchFuseObjects              = 0    # if 0 not fuse
        switchHideObjectsSelected      = 0    # if 0 not fuse
        #### Config End ####

        try:
            selectedEdge     = FreeCADGui.Selection.getSelectionEx()
            sel = selObjects = FreeCADGui.Selection.getSelection()
            subElementName = FreeCADGui.Selection.getSelectionEx()[0].SubElementNames[0] # for color first face selected
            
            try:
                colorFace = App.ActiveDocument.getObject(sel[0].Name).ViewObject.DiffuseColor[int(SubElementName[4:])-1] # color face selected
                ##App.ActiveDocument.getObject(sel[0].Name).ViewObject.DiffuseColor[int(SubElementName[4:])-1] = colorFace# give color on face
            except Exception:
                colorFace = App.ActiveDocument.getObject(sel[0].Name).ViewObject.DiffuseColor[0] # color face selected [0] 

            if (str(sel[0].Shape.ShapeType) != "Face") and (str(sel[1].Shape.ShapeType) != "Face"):
                print("1 ShapeFace ShapeFace")
                sel00 = sel[0]
                sel01 = sel[1]
                ### Begin command Part_ElementCopy First selection
                newFace1 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face1').Shape = newFace1
                shapeFace1 = App.ActiveDocument.ActiveObject
                ####
                ### Begin command Part_ElementCopy Second selection
                newFace2 = Part.getShape(App.ActiveDocument.getObject(sel01.Name),selectedEdge[1].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.recompute()
                App.ActiveDocument.addObject('Part::Feature','Face2').Shape = newFace2
                shapeFace2 = App.ActiveDocument.ActiveObject
                App.ActiveDocument.recompute()
                ### End command Part_ElementCopy

                ### Begin command Part_Loft
                attached = App.ActiveDocument.addObject('Part::Loft','Attached')
                attached.Sections = [App.ActiveDocument.getObject(shapeFace1.Name), App.ActiveDocument.getObject(shapeFace2.Name), ]
                attached.Solid=True
                attached.Ruled=False
                attached.Closed=False
                App.ActiveDocument.recompute()
                ### End command Part_Loft

                ### Begin command Part_Fuse
                if switchFuseObjects == 1:
                    fusionEnsemble = App.ActiveDocument.addObject("Part::MultiFuse","Fusion")
                    try:                # multiple objects
                        App.ActiveDocument.getObject(fusionEnsemble.Name).Shapes = [App.ActiveDocument.getObject(sel00.Name),App.ActiveDocument.getObject(attached.Name),App.ActiveDocument.getObject(sel01.Name),]
                        fusionShapes = App.ActiveDocument.ActiveObject
                    except Exception:   # single object
                        try:
                            App.ActiveDocument.getObject(fusionEnsemble.Name).Shapes = [App.ActiveDocument.getObject(sel[0].Name),App.ActiveDocument.Attached,] #App.ActiveDocument.getObject(sel00.Name),]
                            fusionShapes = App.ActiveDocument.ActiveObject
                        except Exception:
                            None
                    App.ActiveDocument.recompute()
                    ### End command Part_Fuse
                    
                    # create single object
                    Part.show(fusionShapes.Shape.copy())
                    App.ActiveDocument.recompute()
            
                # hidde construction faces
                App.ActiveDocument.getObject(shapeFace1.Name).ViewObject.Visibility = False
                App.ActiveDocument.getObject(shapeFace2.Name).ViewObject.Visibility = False
                if switchHideObjectsSelected == 1:
                    App.ActiveDocument.getObject(sel00.Name).ViewObject.Visibility = False
                    App.ActiveDocument.getObject(sel01.Name).ViewObject.Visibility = False

                if switchRemoveConstructionObject == 1:
                    App.ActiveDocument.removeObject(attached.Name)
                    try:
                        App.ActiveDocument.removeObject(fusionShapes.Name)
                    except Exception:
                        None
                    App.ActiveDocument.removeObject(shapeFace1.Name)
                    App.ActiveDocument.removeObject(shapeFace2.Name)

                App.ActiveDocument.ActiveObject.ViewObject.DiffuseColor = colorFace    # give face color on object
                App.ActiveDocument.ActiveObject.Label = sel[0].Label + "_" + subElementName

            elif (str(sel[0].Shape.ShapeType) != "Face") and (str(sel[1].Shape.ShapeType) == "Face"):
                print("2 ShapeFace Face")
                sel00 = sel[0]
                sel01 = sel[1]
                ### Begin command Part_ElementCopy First selection
                newFace1 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face1').Shape = newFace1
                shapeFace1 = App.ActiveDocument.ActiveObject
                ### End command Part_ElementCopy

                ### Begin command Part_ElementCopy Second selection
                newFace2 = Part.getShape(App.ActiveDocument.getObject(sel01.Name),selectedEdge[1].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face2').Shape = newFace2
                shapeFace2 = App.ActiveDocument.ActiveObject
                App.ActiveDocument.recompute()
                ### End command Part_ElementCopy

                ### Begin command Part_Loft
                attached = App.ActiveDocument.addObject('Part::Loft','Attached')
                attached.Sections = [App.ActiveDocument.getObject(shapeFace1.Name), App.ActiveDocument.getObject(shapeFace2.Name), ]
                attached.Solid=True
                attached.Ruled=False
                attached.Closed=False
                App.ActiveDocument.recompute()
                ### End command Part_Loft

                ### Begin command Part_Fuse
                if switchFuseObjects == 1:
                    fusionEnsemble = App.ActiveDocument.addObject("Part::MultiFuse","Fusion")
                    App.ActiveDocument.getObject(fusionEnsemble.Name).Shapes = [App.ActiveDocument.getObject(sel00.Name),App.ActiveDocument.getObject(attached.Name),] #App.ActiveDocument.getObject(sel01.Name),]
                    fusionShapes = App.ActiveDocument.ActiveObject
                    App.ActiveDocument.recompute()
                ### End command Part_Fuse
                
                ### create single object
                    Part.show(fusionShapes.Shape.copy())
                    App.ActiveDocument.recompute()

                # hidde construction faces
                App.ActiveDocument.getObject(shapeFace1.Name).ViewObject.Visibility = False
                App.ActiveDocument.getObject(shapeFace2.Name).ViewObject.Visibility = False
                if switchHideObjectsSelected == 1:
                    App.ActiveDocument.getObject(sel00.Name).ViewObject.Visibility = False
                    App.ActiveDocument.getObject(sel01.Name).ViewObject.Visibility = False

                if switchRemoveConstructionObject == 1:
                    App.ActiveDocument.removeObject(attached.Name)
                    try:
                        App.ActiveDocument.removeObject(fusionShapes.Name)
                    except Exception:
                        None
                    App.ActiveDocument.removeObject(shapeFace1.Name)
                    App.ActiveDocument.removeObject(shapeFace2.Name)

                App.ActiveDocument.ActiveObject.ViewObject.DiffuseColor = colorFace    # give face color on object
                App.ActiveDocument.ActiveObject.Label = sel[0].Label + "_" + subElementName

            elif (str(sel[0].Shape.ShapeType) == "Face") and (str(sel[1].Shape.ShapeType) != "Face"):
                print("3 Face ShapeFace")
                sel00 = sel[0]
                sel01 = sel[1]
                ### Begin command Part_ElementCopy First selection
                newFace1 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face1').Shape = newFace1
                shapeFace1 = App.ActiveDocument.ActiveObject
                ### End command Part_ElementCopy

                ### Begin command Part_ElementCopy Second selection
                newFace2 = Part.getShape(App.ActiveDocument.getObject(sel01.Name),selectedEdge[1].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face2').Shape = newFace2
                shapeFace2 = App.ActiveDocument.ActiveObject
                App.ActiveDocument.recompute()
                ### End command Part_ElementCopy

                ### Begin command Part_Loft
                attached = App.ActiveDocument.addObject('Part::Loft','Attached')
                attached.Sections = [App.ActiveDocument.getObject(shapeFace1.Name), App.ActiveDocument.getObject(shapeFace2.Name), ]
                attached.Solid=True
                attached.Ruled=False
                attached.Closed=False
                App.ActiveDocument.recompute()
                ### End command Part_Loft

                ### Begin command Part_Fuse
                if switchFuseObjects == 1:
                    fusionEnsemble = App.ActiveDocument.addObject("Part::MultiFuse","Fusion")
                    App.ActiveDocument.getObject(fusionEnsemble.Name).Shapes = [App.ActiveDocument.getObject(sel01.Name),App.ActiveDocument.getObject(attached.Name),] #App.ActiveDocument.getObject(sel01.Name),]
                    fusionShapes = App.ActiveDocument.ActiveObject
                    App.ActiveDocument.recompute()
                ### End command Part_Fuse
                
                ### create single object
                    Part.show(fusionShapes.Shape.copy())
                    App.ActiveDocument.recompute()

                # hidde construction faces
                App.ActiveDocument.getObject(shapeFace1.Name).ViewObject.Visibility = False
                App.ActiveDocument.getObject(shapeFace2.Name).ViewObject.Visibility = False
                if switchHideObjectsSelected == 1:
                    App.ActiveDocument.getObject(sel00.Name).ViewObject.Visibility = False
                    App.ActiveDocument.getObject(sel01.Name).ViewObject.Visibility = False

                if switchRemoveConstructionObject == 1:
                    App.ActiveDocument.removeObject(attached.Name)
                    try:
                        App.ActiveDocument.removeObject(fusionShapes.Name)
                    except Exception:
                        None
                    App.ActiveDocument.removeObject(shapeFace1.Name)
                    App.ActiveDocument.removeObject(shapeFace2.Name)

                App.ActiveDocument.ActiveObject.ViewObject.DiffuseColor = colorFace    # give face color on object
                App.ActiveDocument.ActiveObject.Label = sel[0].Label + "_" + subElementName

            elif (str(sel[0].Shape.ShapeType) == "Face") and (str(sel[1].Shape.ShapeType) == "Face"):
                print("4 Face Face")
                sel00 = sel[0]
                sel01 = sel[1]
                ### Begin command Part_ElementCopy First selection
                newFace1 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[0],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face1').Shape = newFace1
                shapeFace1 = App.ActiveDocument.ActiveObject
                ####
                ### Begin command Part_ElementCopy Second selection
                try:# independent object 
                    newFace2 = Part.getShape(App.ActiveDocument.getObject(sel01.Name),selectedEdge[1].SubElementNames[0],needSubElement=True,refine=False).copy()
                except Exception:
                    # same object other face
                    newFace2 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[1],needSubElement=True,refine=False).copy()
                App.ActiveDocument.addObject('Part::Feature','Face2').Shape = newFace2
                shapeFace2 = App.ActiveDocument.ActiveObject
                App.ActiveDocument.recompute()
                ### End command Part_ElementCopy

                ### Begin command Part_Loft
                attached = App.ActiveDocument.addObject('Part::Loft','Attached')
                attached.Sections = [App.ActiveDocument.getObject(shapeFace1.Name), App.ActiveDocument.getObject(shapeFace2.Name), ]
                attached.Solid=True
                attached.Ruled=False
                attached.Closed=False
                App.ActiveDocument.recompute()
                ### End command Part_Loft

                # create single object
                Part.show(attached.Shape.copy())
                App.ActiveDocument.recompute()

                # hidde construction faces
                App.ActiveDocument.getObject(shapeFace1.Name).ViewObject.Visibility = False
                App.ActiveDocument.getObject(shapeFace2.Name).ViewObject.Visibility = False
                if switchHideObjectsSelected == 1:
                    App.ActiveDocument.getObject(sel00.Name).ViewObject.Visibility = False
                    App.ActiveDocument.getObject(sel01.Name).ViewObject.Visibility = False

                if switchRemoveConstructionObject == 1:
                    App.ActiveDocument.removeObject(attached.Name)
                    App.ActiveDocument.removeObject(shapeFace1.Name)
                    App.ActiveDocument.removeObject(shapeFace2.Name)

                App.ActiveDocument.ActiveObject.ViewObject.DiffuseColor = colorFace    # give face color on object
                App.ActiveDocument.ActiveObject.Label = sel[0].Label + "_" + subElementName

        except Exception:
                try:
                    sel00 = sel[0]
                    print("5 ShapeFace ShapeFace same object")
                    ### Begin command Part_ElementCopy First selection
                    newFace1 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[0],needSubElement=True,refine=False).copy()
                    App.ActiveDocument.addObject('Part::Feature','Face1').Shape = newFace1
                    shapeFace1 = App.ActiveDocument.ActiveObject
                    ####
            
                    ### Begin command Part_ElementCopy Second selection
                    newFace2 = Part.getShape(App.ActiveDocument.getObject(sel00.Name),selectedEdge[0].SubElementNames[1],needSubElement=True,refine=False).copy()
                    App.ActiveDocument.recompute()
                    App.ActiveDocument.addObject('Part::Feature','Face2').Shape = newFace2
                    shapeFace2 = App.ActiveDocument.ActiveObject
                    App.ActiveDocument.recompute()
                    ### End command Part_ElementCopy
            
                    ### Begin command Part_Loft
                    attached = App.ActiveDocument.addObject('Part::Loft','Attached')
                    attached.Sections = [App.ActiveDocument.getObject(shapeFace1.Name), App.ActiveDocument.getObject(shapeFace2.Name), ]
                    attached.Solid=True
                    attached.Ruled=False
                    attached.Closed=False
                    App.ActiveDocument.recompute()
                    ### End command Part_Loft
            
                    ### Begin command Part_Fuse
                    if switchFuseObjects == 1:
                        fusionEnsemble = App.ActiveDocument.addObject("Part::MultiFuse","Fusion")
                        App.ActiveDocument.getObject(fusionEnsemble.Name).Shapes = [App.ActiveDocument.getObject(sel[0].Name),App.ActiveDocument.Attached,] #App.ActiveDocument.getObject(sel00.Name),]
                        fusionShapes = App.ActiveDocument.ActiveObject
                        App.ActiveDocument.recompute()
                        ### End command Part_Fuse
                        
                        # create single object
                        Part.show(fusionShapes.Shape.copy())
                        App.ActiveDocument.recompute()
                
                    # hidde construction faces
                    App.ActiveDocument.getObject(shapeFace1.Name).ViewObject.Visibility = False
                    App.ActiveDocument.getObject(shapeFace2.Name).ViewObject.Visibility = False
                    if switchHideObjectsSelected == 1:
                        App.ActiveDocument.getObject(sel00.Name).ViewObject.Visibility = False
            
                    if switchRemoveConstructionObject == 1:
                        App.ActiveDocument.removeObject(attached.Name)
                        try: 
                            App.ActiveDocument.removeObject(fusionShapes.Name)
                        except Exceptions:
                            None
                        App.ActiveDocument.removeObject(shapeFace1.Name)
                        App.ActiveDocument.removeObject(shapeFace2.Name)
            
                    App.ActiveDocument.ActiveObject.ViewObject.DiffuseColor = colorFace    # give face color on object
                    App.ActiveDocument.ActiveObject.Label = sel[0].Label + "_" + subElementName
                except Exception:
                    print("Oups")
                    None
        #################################################################################################
    def askQuestion(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes |QtGui.QMessageBox.No)
        msgBox.setInformativeText("Remove old objects?")
        t= msgBox.exec_()
        if t== QtGui.QMessageBox.Yes:
            return 1
        else: 
            return 0

        #################################################################################################

    def GetResources(self):
            return{
            'Pixmap':    Design456Init.ICON_PATH + '/unifySplitFuse1.svg',
            'MenuText': 'unify-Split & Fuse',
            'ToolTip':  'unify Split and Fuse'
        }
            
Gui.addCommand('Design456_unifySplitFuse1', Design456_unifySplitFuse1())



class Design456_unifySplitFuse2:
    def Activated(self):
        try:
            sel = Gui.Selection.getSelection()
            if (len(sel) != 2):
                # Two object must be selected
                errMessage = "Select two objects to use the Tool"
                faced.getInfo(sel).errorDialog(errMessage)
                return
            reply = self.askQuestion()
            Gui.ActiveDocument.getObject(sel[0].Name).Visibility=False
            Gui.ActiveDocument.getObject(sel[1].Name).Visibility=False

            #### Config Begin ####

            switchRemoveConstructionObject = self.askQuestion()    # if 0 (NO) not removed creation objects 1= (YES) remove objects
            colorCommon = (0.9373, 0.1608, 0.1608)
            colorCut1   = (0.4471, 0.6235, 0.8118)
            colorCut2   = (0.0235, 0.6902, 0.6902)
            colorFuse   = (1.0000, 0.6667, 0.0000)
            #### Config End ####

            ##### Begin command _part_Common
            #### create copy
            shapeCommon = _part.getShape(App.ActiveDocument.getObject(sel[0].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Common1').Shape = shapeCommon
            newObjectCut_A1 = App.ActiveDocument.ActiveObject
            shapeCommon = _part.getShape(App.ActiveDocument.getObject(sel[1].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Common2').Shape = shapeCommon
            newObjectCut_A2 = App.ActiveDocument.ActiveObject
            ####
            commonObject     = App.ActiveDocument.addObject("Part::MultiCommon","Common")
            commonObjectMake = App.ActiveDocument.getObject(commonObject.Name).Shapes = [App.ActiveDocument.getObject(newObjectCut_A1.Name), App.ActiveDocument.getObject(newObjectCut_A2.Name),]
            shapeCommonMake  = App.ActiveDocument.ActiveObject
            App.ActiveDocument.recompute()
            Gui.ActiveDocument.activeObject().ShapeColor = colorCommon
            ####
            shapeCommon = _part.getShape(App.ActiveDocument.getObject(shapeCommonMake.Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','shapeCommon').Shape = shapeCommon
            Gui.ActiveDocument.activeObject().ShapeColor = colorCommon
            if switchRemoveConstructionObject == 1:
                App.ActiveDocument.removeObject(shapeCommonMake.Name)
                App.ActiveDocument.removeObject(newObjectCut_A1.Name)
                App.ActiveDocument.removeObject(newObjectCut_A2.Name)
            #### End command Part_Common

            #### Begin command Part_Cut First
            #### create copy
            shapeCut1 = _part.getShape(App.ActiveDocument.getObject(sel[0].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Cut01').Shape = shapeCut1
            newObjectCut_A1 = App.ActiveDocument.ActiveObject
            shapeCut1 = _part.getShape(App.ActiveDocument.getObject(sel[1].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Cut02').Shape = shapeCut1
            newObjectCut_A2 = App.ActiveDocument.ActiveObject
            ####
            App.ActiveDocument.addObject("Part::Cut","Cut_01")
            App.ActiveDocument.Cut_01.Base = App.ActiveDocument.getObject(newObjectCut_A1.Name)
            App.ActiveDocument.Cut_01.Tool = App.ActiveDocument.getObject(newObjectCut_A2.Name)
            shapeCutMake  = App.ActiveDocument.ActiveObject
            App.ActiveDocument.recompute()
            Gui.ActiveDocument.activeObject().ShapeColor = colorCut1
            ####
            shapeCut01 = _part.getShape(App.ActiveDocument.getObject(shapeCutMake.Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','shapeCut01').Shape = shapeCut01
            Gui.ActiveDocument.activeObject().ShapeColor = colorCut1
            if switchRemoveConstructionObject == 1:
                App.ActiveDocument.removeObject(shapeCutMake.Name)
                App.ActiveDocument.removeObject(newObjectCut_A1.Name)
                App.ActiveDocument.removeObject(newObjectCut_A2.Name)
            #### End command Part_Cut First

            #### Begin command Part_Cut Second
            #### create copy
            shapeCut2 = _part.getShape(App.ActiveDocument.getObject(sel[1].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Cut01').Shape = shapeCut2
            newObjectCut_A1 = App.ActiveDocument.ActiveObject
            shapeCut2 = _part.getShape(App.ActiveDocument.getObject(sel[0].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Cut02').Shape = shapeCut2
            newObjectCut_A2 = App.ActiveDocument.ActiveObject
            ####
            App.ActiveDocument.addObject("Part::Cut","Cut_02")
            App.ActiveDocument.Cut_02.Base = App.ActiveDocument.getObject(newObjectCut_A1.Name)
            App.ActiveDocument.Cut_02.Tool = App.ActiveDocument.getObject(newObjectCut_A2.Name)
            shapeCutMake  = App.ActiveDocument.ActiveObject
            App.ActiveDocument.recompute()
            Gui.ActiveDocument.activeObject().ShapeColor = colorCut2
            ####
            shapeCut02 = _part.getShape(App.ActiveDocument.getObject(shapeCutMake.Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','shapeCut02').Shape = shapeCut02
            Gui.ActiveDocument.activeObject().ShapeColor = colorCut2
            if switchRemoveConstructionObject == 1:
                App.ActiveDocument.removeObject(shapeCutMake.Name)
                App.ActiveDocument.removeObject(newObjectCut_A1.Name)
                App.ActiveDocument.removeObject(newObjectCut_A2.Name)
            #### End command Part_Cut Second

            #### Begin command Part_Fuse
            #### create copy
            shapeFuse1 = _part.getShape(App.ActiveDocument.getObject(sel[1].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Fuse01').Shape = shapeFuse1
            newObjectFuse1 = App.ActiveDocument.ActiveObject
            shapeFuse2 = _part.getShape(App.ActiveDocument.getObject(sel[0].Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','Fuse02').Shape = shapeFuse2
            newObjectFuse2 = App.ActiveDocument.ActiveObject
            ####
            App.ActiveDocument.addObject("Part::MultiFuse","Fusion")
            App.ActiveDocument.Fusion.Shapes = [App.ActiveDocument.getObject(newObjectFuse1.Name),App.ActiveDocument.getObject(newObjectFuse2.Name),]
            shapeCutFusion  = App.ActiveDocument.ActiveObject
            App.ActiveDocument.recompute()
            Gui.ActiveDocument.activeObject().ShapeColor = colorFuse
            ####
            shapeFusion = _part.getShape(App.ActiveDocument.getObject(shapeCutFusion.Name),'',needSubElement=False,refine=False)
            App.ActiveDocument.addObject('Part::Feature','shapeFusion').Shape = shapeFusion
            Gui.ActiveDocument.activeObject().ShapeColor = colorFuse
            if switchRemoveConstructionObject == 1:
                App.ActiveDocument.removeObject(shapeCutFusion.Name)
                App.ActiveDocument.removeObject(newObjectFuse1.Name)
                App.ActiveDocument.removeObject(newObjectFuse2.Name)
            #### End command Part_Fuse

        except Exception as err:
            App.Console.PrintError("'makeIt' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    def askQuestion(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes |QtGui.QMessageBox.No)
        msgBox.setInformativeText("Remove old objects?")
        t= msgBox.exec_()
        if t== QtGui.QMessageBox.Yes:
            return 1
        else: 
            return 0
    def GetResources(self):
            return{
            'Pixmap':    Design456Init.ICON_PATH + '/UnifySplitFuse2.svg',
            'MenuText': 'unify-Split & Fuse 2',
            'ToolTip':  'unify Split and Fuse2'
        }
Gui.addCommand('Design456_unifySplitFuse2', Design456_unifySplitFuse2())