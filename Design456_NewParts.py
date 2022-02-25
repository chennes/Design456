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
import ImportGui
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui, QtCore  # https://www.freecadweb.org/wiki/PySide
import Draft
import Part
from draftutils.translate import translate   #for translate
import Design456Init
import FACE_D as faced
import DraftGeomUtils
__updated__ = '2022-02-25 21:03:38'


#Roof

class ViewProviderRoof:

    obj_name = "Roof"

    def __init__(self, obj, obj_name):
        self.obj_name = ViewProviderRoof.obj_name
        obj.Proxy = self

    def attach(self, obj):
        return

    def updateData(self, fp, prop):
        return

    def getDisplayModes(self, obj):
        return "As Is"

    def getDefaultDisplayMode(self):
        return "As Is"

    def setDisplayMode(self, mode):
        return "As Is"

    def onChanged(self, vobj, prop):
        pass

    def getIcon(self):
        return ( Design456Init.ICON_PATH + 'Roof.svg')

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None


#Roof 
class Design456_Roof:
    """ Roof shape based on several parameters
    """
    def __init__(self, obj, 
                       width=20,
                       length=20,
                       height=10,
                       thickness=1):


        obj.addProperty("App::PropertyLength", "Width","Roof", 
                        "Width of the Roof").Width = width

        obj.addProperty("App::PropertyLength", "Length","Roof", 
                        "Length of the Roof").Length = length

        obj.addProperty("App::PropertyLength", "Height","Roof", 
                        "Height of the Roof").Height = height

        obj.addProperty("App::PropertyLength", "Thickness","Roof", 
                        "Thickness of the Roof").Thickness = thickness
        obj.Proxy = self
    
    def execute(self, obj):
        self.Width=float(obj.Width)
        self.Height=float(obj.Height)
        self.Length=float(obj.Length)
        self.Thickness=float(obj.Thickness)
        vert1=[App.Vector(0,0,0),App.Vector(self.Width,0,0),
                App.Vector(self.Width/2,0.0,self.Height),
                App.Vector(0,0,0)]
        newWidth=self.Width-2*self.Thickness
        newLength=self.Length-2*self.Thickness
        newHeight=self.Height-self.Thickness
        vert2=[App.Vector(self.Thickness,self.Thickness,0),App.Vector(self.Thickness+newWidth,self.Thickness,0),
               App.Vector(self.Width/2,self.Thickness,newHeight),
               App.Vector(self.Thickness,self.Thickness,0)]
        FaceTriangle1=Part.Face(Part.makePolygon(vert1))
        obj1 =FaceTriangle1.extrude(App.Vector(0.0,self.Length,0.0))
        
        FaceTriangle2=Part.Face(Part.makePolygon(vert2))
        obj2= FaceTriangle2.extrude(App.Vector(0.0,self.Length-2*self.Thickness,0.0))
        Result = obj1.cut(obj2)
        obj.Shape=Result
        
class Design456_Seg_Roof:
    def GetResources(self):
        return {'Pixmap':Design456Init.ICON_PATH + 'Roof.svg',
                'MenuText': "Roof",
                'ToolTip': "Generate a Roof"}

    def Activated(self):
        newObj = App.ActiveDocument.addObject(
            "Part::FeaturePython", "Roof")
        Design456_Roof(newObj)

        ViewProviderRoof(newObj.ViewObject, "Roof")

        App.ActiveDocument.recompute()
        v = Gui.ActiveDocument.ActiveView
        faced.PartMover(v, newObj, deleteOnEscape=True)

Gui.addCommand('Design456_Seg_Roof', Design456_Seg_Roof())


#***************************



#Housing

class ViewProviderHousing:

    obj_name = "Housing"

    def __init__(self, obj, obj_name):
        self.obj_name = ViewProviderHousing.obj_name
        obj.Proxy = self

    def attach(self, obj):
        return

    def updateData(self, fp, prop):
        return

    def getDisplayModes(self, obj):
        return "As Is"

    def getDefaultDisplayMode(self):
        return "As Is"

    def setDisplayMode(self, mode):
        return "As Is"

    def onChanged(self, vobj, prop):
        pass

    def getIcon(self):
        return ( Design456Init.ICON_PATH + 'Housing.svg')

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None


#Housing 
class Design456_HousingBase:
    """ Housing shape based on several parameters
    """
    def __init__(self, obj, 
                       width=20,
                       length=20,
                       height=10,
                       thickness=1):


        obj.addProperty("App::PropertyLength", "Width","Housing", 
                        "Width of the Housing").Width = width

        obj.addProperty("App::PropertyLength", "Length","Housing", 
                        "Length of the Housing").Length = length

        obj.addProperty("App::PropertyLength", "Height","Housing", 
                        "Height of the Housing").Height = height

        obj.addProperty("App::PropertyLength", "Thickness","Housing", 
                        "Thickness of the Housing").Thickness = thickness
        obj.Proxy = self
    
    def execute(self, obj):
        self.Width=float(obj.Width)
        self.Height=float(obj.Height)
        self.Length=float(obj.Length)
        self.Thickness=float(obj.Thickness)
        Result=None
        V1_FSQ=[App.Vector(0,0,0),
                 App.Vector(self.Width,0,0),
                 App.Vector(self.Width,self.Length,0),
                 App.Vector(0.0,self.Length,0),
                 App.Vector(0,0,0)]

        V2_FSQ=[App.Vector(self.Thickness,self.Thickness,0),
                 App.Vector(self.Width-self.Thickness,self.Thickness,0),
                 App.Vector(self.Width-self.Thickness,self.Length-self.Thickness,0),
                 App.Vector(self.Thickness,self.Length-self.Thickness,0),
                 App.Vector(self.Thickness,self.Thickness,0)]
        firstFace1=Part.Face(Part.makePolygon(V1_FSQ))  # one used with secondFace to cut
        firstFace2=Part.Face(Part.makePolygon(V1_FSQ))  # Other used to make the bottom
        secondFace=Part.Face(Part.makePolygon(V2_FSQ))
        resultButtom=firstFace1.cut(secondFace)
        extrude1=resultButtom.extrude(App.Vector(0,0,self.Height))
        extrude2=firstFace2.extrude(App.Vector(0,0,self.Thickness))
        fused=extrude1.fuse(extrude2)
        Result=fused.removeSplitter()
        obj.Shape=Result
        
class Design456_Housing:
    def GetResources(self):
        return {'Pixmap':Design456Init.ICON_PATH + 'Housing.svg',
                'MenuText': "Housing",
                'ToolTip': "Generate a Housing"}

    def Activated(self):
        newObj = App.ActiveDocument.addObject(
            "Part::FeaturePython", "Housing")
        Design456_HousingBase(newObj)

        ViewProviderHousing(newObj.ViewObject, "Housing")

        App.ActiveDocument.recompute()
        v = Gui.ActiveDocument.ActiveView
        faced.PartMover(v, newObj, deleteOnEscape=True)

Gui.addCommand('Design456_Housing', Design456_Housing())





#RoundedHousing

class ViewProviderRoundedHousing:

    obj_name = "RoundedHousing"

    def __init__(self, obj, obj_name):
        self.obj_name = ViewProviderRoundedHousing.obj_name
        obj.Proxy = self

    def attach(self, obj):
        return

    def updateData(self, fp, prop):
        return

    def getDisplayModes(self, obj):
        return "As Is"

    def getDefaultDisplayMode(self):
        return "As Is"

    def setDisplayMode(self, mode):
        return "As Is"

    def onChanged(self, vobj, prop):
        pass

    def getIcon(self):
        return ( Design456Init.ICON_PATH + 'RoundedHousing.svg')

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None

################################


#RoundedHousing 
class Design456_RoundedHousingBase:
    """ RoundedHousing shape based on several parameters
    """
    def __init__(self, obj, 
                       width=20,
                       length=20,
                       height=10,
                       radius=1,
                       thickness=1,chamfer=False):


        obj.addProperty("App::PropertyLength", "Width","RoundedHousing", 
                        "Width of the RoundedHousing").Width = width

        obj.addProperty("App::PropertyLength", "Length","RoundedHousing", 
                        "Length of the RoundedHousing").Length = length

        obj.addProperty("App::PropertyLength", "Height","RoundedHousing", 
                        "Height of the RoundedHousing").Height = height

        obj.addProperty("App::PropertyLength", "Radius","RoundedHousing", 
                        "Height of the RoundedHousing").Radius = radius

        obj.addProperty("App::PropertyLength", "Thickness","RoundedHousing", 
                        "Thickness of the RoundedHousing").Thickness = thickness

        obj.addProperty("App::PropertyBool", "Chamfer","RoundedHousing", 
                        "Chamfer corner").Chamfer = chamfer
        obj.Proxy = self
    
    def execute(self, obj):
        self.Width=float(obj.Width)
        self.Height=float(obj.Height)
        self.Length=float(obj.Length)
        self.Radius=float(obj.Radius)
        self.Thickness=float(obj.Thickness)
        self.Chamfer=obj.Chamfer
        Result=None
        # base rectangle vertices and walls after a cut
        V1_FSQ=[App.Vector(0,0,0),
                App.Vector(self.Width,0,0),
                App.Vector(self.Width,self.Length,0),
                App.Vector(0.0,self.Length,0),
                App.Vector(0,0,0)]

        # cut middle part to make walls
        V2_FSQ=[App.Vector(self.Thickness,self.Thickness,0),
                App.Vector(self.Width-self.Thickness,self.Thickness,0),
                App.Vector(self.Width-self.Thickness,self.Length-self.Thickness,0),
                App.Vector(self.Thickness,self.Length-self.Thickness,0),
                App.Vector(self.Thickness,self.Thickness,0)]
        
        W1=Part.makePolygon(V1_FSQ)
        W11 = DraftGeomUtils.filletWire(W1,self.Radius, chamfer=self.Chamfer)
        
        firstFace1=Part.Face(W11)  # one used with secondFace to cut
        firstFace2=firstFace1.copy()  # Other used to make the bottom

        W2=Part.makePolygon(V2_FSQ)
        W22 = DraftGeomUtils.filletWire(W2,self.Radius, chamfer=False)
        
        secondFace=Part.Face(W22)

        resultButtom=firstFace1.cut(secondFace)
        extrude1=resultButtom.extrude(App.Vector(0,0,self.Height))
        extrude2=firstFace2.extrude(App.Vector(0,0,self.Thickness))
        fused=extrude1.fuse(extrude2)
        Result=fused.removeSplitter()
        obj.Shape=Result
        
class Design456_RoundedHousing:
    def GetResources(self):
        return {'Pixmap':Design456Init.ICON_PATH + 'RoundedHousing.svg',
                'MenuText': "RoundedHousing",
                'ToolTip': "Generate a RoundedHousing"}

    def Activated(self):
        newObj = App.ActiveDocument.addObject(
            "Part::FeaturePython", "RoundedHousing")
        Design456_RoundedHousingBase(newObj)

        ViewProviderRoundedHousing(newObj.ViewObject, "RoundedHousing")

        App.ActiveDocument.recompute()
        v = Gui.ActiveDocument.ActiveView
        faced.PartMover(v, newObj, deleteOnEscape=True)

Gui.addCommand('Design456_RoundedHousing', Design456_RoundedHousing())

