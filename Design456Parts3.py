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
from draftutils.translate import translate  # for translate
import Design456Init
import FACE_D as faced
import DraftGeomUtils
import math
import BOPTools.SplitFeatures

__updated__ = '2022-09-11 22:03:54'


#TODO : FIXME: 
# Fence

class ViewProviderFence:

    obj_name = "Fence"

    def __init__(self, obj, obj_name):
        self.obj_name = ViewProviderFence.obj_name
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
    
    def __getstate__(self):
        return None
    
    def __setstate__(self):
        return None
    
    def getIcon(self):
        return (Design456Init.ICON_PATH + 'Fence.svg')

    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None

class BaseFence:
    """ Fence shape based on several parameters
    """
    Placement=App.Placement()
    def __init__(self, obj,
                 _width=30.00,
                 _height=10.00,
                 _thickness=2,
                 _sections=4,
                 _connectionWidth=1.00,
                 _sectionWidth=2.00,
                 _bottomDistance=1.00,
                 _topDistance=6.00,
                 _sharpLength=1.00,
                 _waveDepth=3.0,
                 _netDistance=0.5,
                 _type=3,
                 ):

        obj.addProperty("App::PropertyLength", "Width", "Fence",
                        "Width of the Fence").Width = _width
                        
        obj.addProperty("App::PropertyLength", "Height", "Fence",
                        "Height of the Fence").Height = _height

        obj.addProperty("App::PropertyLength", "Thickness", "Fence",
                        "Thickness of the Fence").Thickness = _thickness
        
        obj.addProperty("App::PropertyLength", "ConnectionWidth", "Fence",
                        "Connections Width between sections").ConnectionWidth = _connectionWidth

        obj.addProperty("App::PropertyInteger", "Sections", "Sections",
                        "Fence type").Sections = _sections

        obj.addProperty("App::PropertyLength", "SectionWidth", "Sections",
                        "Section Width of the Fence").SectionWidth = _sectionWidth

        obj.addProperty("App::PropertyLength", "waveDepth", "Sections",
                        "Section Width of the Fence").waveDepth = _waveDepth

        obj.addProperty("App::PropertyLength", "BottomDistance", "Fence",
                        "Connection Bottom distance").BottomDistance = _bottomDistance

        obj.addProperty("App::PropertyLength", "TopDistance", "Fence",
                        "Top connection distance").TopDistance = _topDistance

        obj.addProperty("App::PropertyLength", "SharpLength", "Fence",
                        "Sharp part length").SharpLength= _sharpLength
        
        obj.addProperty("App::PropertyLength", "NetDistance", "Fence",
                        "Sharp part length").NetDistance= _netDistance

        obj.addProperty("App::PropertyInteger", "Type", "Fence",
                        "Fence base type").Type = _type
        obj.Proxy = self
        BaseFence.placement=obj.Placement

       
    def oneElementWavedFence(self,Xoffsett,smallWidth,waveOffset):
        CoreStart=(smallWidth-self.SectionWidth)/2
        zOffset=-self.Height/2
        newobj=None
        #Left side         
        p10=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset)

        p11=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)

        p12=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)

        p13=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)

        p14=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)

        p15=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
        
        p16=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
        
        p17=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p18=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p19=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2-self.SharpLength-waveOffset)
        
        p20=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+(self.SectionWidth)/2,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2-waveOffset)
        
        #Right side 

        p39=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2-self.SharpLength-waveOffset)
        
        p38=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)

        
        p37=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p36=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
                                
        p35=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)                                
                                
        p34=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)
        
 
        p33=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)


        p32=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)
        
        p31=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)
        
        p30=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset)
        
 
        newobj=Part.Face(Part.Wire(Part.makePolygon([p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p39,p38,p37,p36,p35,p34,p33,p32,p31,p30,p10])))
        objExtr=newobj.extrude(App.Vector(0,self.Thickness,0))
        return objExtr
    
                
    
    def oneElementNormalFence(self,Xoffsett,smallWidth):
        CoreStart=(smallWidth-self.SectionWidth)/2
        zOffset=-self.Height/2
        newobj=None
        #Left side         
        p10=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset)

        p11=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)

        p12=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)

        p13=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)

        p14=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)

        p15=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
        
        p16=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
        
        p17=App.Vector(BaseFence.Placement.Base.x+Xoffsett,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p18=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p19=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2-self.SharpLength)
        
        p20=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+(self.SectionWidth)/2,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2)
        
        #Right side 

        
        p39=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+self.Height/2-self.SharpLength)
        
        p38=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)

        
        p37=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance+self.ConnectionWidth)
        
        p36=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)
                                
        p35=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.TopDistance)                                
                                
        p34=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)
        
 
        p33=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance+self.ConnectionWidth)


        p32=App.Vector(BaseFence.Placement.Base.x+Xoffsett+smallWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)
        
        p31=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset+self.BottomDistance)
        
        p30=App.Vector(BaseFence.Placement.Base.x+Xoffsett+CoreStart+self.SectionWidth,
                       BaseFence.Placement.Base.y,
                       BaseFence.Placement.Base.z+zOffset)
        
        if self.Type==0:        
            newobj=Part.Face(Part.Wire(Part.makePolygon([p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p39,p38,p37,p36,p35,p34,p33,p32,p31,p30,p10])))
        elif self.Type==1:
            e1=(Part.makePolygon([p10,p11,p12,p13,p14,p15,p16,p17,p18,p19]))
            e2=(Part.ArcOfCircle(p19,p20,p39))
            e3=(Part.makePolygon([p39,p38,p37,p36,p35,p34,p33,p32,p31,p30,p10]))
            newobj=Part.Face(Part.Wire([e1,e2.toShape(),e3]) )
        objExtr=newobj.extrude(App.Vector(0,self.Thickness,0))
        return objExtr
    
    def normalFence(self):
        obj1=None
        try:
            smallWidth=self.Width/self.Sections
            objs=[]
            offset=0
            obj1=self.oneElementNormalFence(offset,smallWidth)
            for i in range(1, self.Sections):
                offset=i*smallWidth
                objs.append(self.oneElementNormalFence(offset,smallWidth))
            if(len(objs)>1):
                return (obj1.fuse(objs)).removeSplitter()
            else:
                return obj1.removeSplitter()
            
        except Exception as err:
            App.Console.PrintError("'createObject Fence' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
    def wavedFence(self):
        #Wavy length
        try:
            smallWidth=self.Width/self.Sections          
            objs=[]
            offset=0
            angle=math.radians(180/(self.Sections-1))
            angels=[]
            if (self.Sections/2 ==int(self.Sections/2)):
                for i in range(0,int(self.Sections/2)-1):
                  angels.append(angle*i)
                angels.append(angle*self.Sections/2)
                angels.append(angle*self.Sections/2)
                for i in range(int(self.Sections/2)+1,self.Sections):
                  angels.append(angle*i)
            else:
                for i in range(0,self.Sections):
                  angels.append(angle*i)
            for i in range(0, self.Sections):
                offset=(i*smallWidth)
                objs.append(self.oneElementWavedFence(offset,smallWidth,abs(self.waveDepth*math.cos(angels[i]))))

            obj1=objs[0]
            objs.pop(0)  #Remove it from the list to allow fuse without problem
            if(len(objs)>1):
                return (obj1.fuse(objs)).removeSplitter()
            else:
                return obj1.removeSplitter()
    
        except Exception as err:
            App.Console.PrintError("'createObject Fence' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
 
    def NetFence(self):
        try:
            smallWidth=self.Width/self.Sections          
            objs=[]
            offset=0
            obj1=None
            '''
                            p1  p8                              p4                    
                                                        p5      
                            
                                p7                      p6      
                            p2                                   p3
            '''
            p1=App.Vector(BaseFence.Placement.Base.x, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z+self.Height/2)
            p2=App.Vector(BaseFence.Placement.Base.x, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z-self.Height/2)
            p3=App.Vector(BaseFence.Placement.Base.x+self.Width, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z-self.Height/2)
            p4=App.Vector(BaseFence.Placement.Base.x+self.Width, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z+self.Height/2)
            
            p5=App.Vector(BaseFence.Placement.Base.x+self.Width-self.SectionWidth, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z+self.Height/2)            
            p6=App.Vector(BaseFence.Placement.Base.x+self.Width-self.SectionWidth, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z-self.Height/2+self.SectionWidth)
            p7=App.Vector(BaseFence.Placement.Base.x+self.SectionWidth, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z-self.Height/2+self.SectionWidth)
            p8=App.Vector(BaseFence.Placement.Base.x+self.SectionWidth, BaseFence.Placement.Base.y,BaseFence.Placement.Base.z+self.Height/2)            

            #Lines will have self.netDistance width and will have space of the same size
            NrOfNetLines=int(self.Height/(self.NetDistance))
            
            TopInnerPointLeft =p8
            TopInnerPointRight=p5

            BottomInnerPointLeft=p7
            BottomInnerPointRight=p6
            oneSeg=[]
            netObj=[]
            _height=self.Width-self.SectionWidth*2
            step=self.NetDistance
            step1=self.NetDistance*2
            xChange1=0
            xChange2=0
            while (_height>step1):
                oneSeg.clear()
                if step<= self.Height:
                    h1=step
                else:
                    h1=self.Height
                    xChange1=xChange1+self.NetDistance
                if step1<= self.Height:
                    h2=step1
                else:
                    h2=self.Height
                    xChange2=xChange2+self.NetDistance*2
                    
                oneSeg.append(BottomInnerPointLeft+App.Vector(xChange1,0, h1))
                oneSeg.append(BottomInnerPointLeft+App.Vector(xChange2,0, h2))
                oneSeg.append(BottomInnerPointLeft+App.Vector(step1,0, 0))
                oneSeg.append(BottomInnerPointLeft+App.Vector(step,0, 0))
                
                # oneSeg.append(BottomInnerPointRight+App.Vector(0,0, step))
                # oneSeg.append(BottomInnerPointRight+App.Vector(0,0, step1))
                # oneSeg.append(BottomInnerPointRight+App.Vector(-step,0, 0))
                # oneSeg.append(BottomInnerPointRight+App.Vector(-step1,0, 0))

                
                netObj.append(Part.Face(Part.makePolygon([*oneSeg,oneSeg[0]])))
                print(oneSeg)
                step=step+self.NetDistance*2
                step1=step1+self.NetDistance*2
                
            obj1=Part.Face(Part.Wire(Part.makePolygon([p1,p2,p3,p4,p5,p6,p7,p8,p1])))
            allObjects=obj1.fuse(netObj)
            objNew=allObjects.extrude(App.Vector(0,self.Thickness,0))
            return objNew.removeSplitter()
    
        except Exception as err:
            App.Console.PrintError("'createObject Fence' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
    def createObject(self):
        try:
            finalObj=None
            if self.Type==0 or self.Type==1:
                finalObj=self.normalFence()
            elif self.Type==2:
                finalObj=self.wavedFence()
            elif self.Type==3:
                finalObj=self.NetFence()
            elif self.Type==4:
                pass
            return finalObj
        except Exception as err:
            App.Console.PrintError("'execute Fence' Failed. "
                                   "{err}\n".format(err=str(err)))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            
    def execute(self, obj):


        self.Width = float(obj.Width)        
        self.Height = int(obj.Height)
        self.Thickness = int(obj.Thickness)
        self.SectionWidth = float(obj.SectionWidth)
        self.Type = int(obj.Type)
        self.BottomDistance = float(obj.BottomDistance)
        self.TopDistance = float(obj.TopDistance)
        self.SharpLength = float(obj.SharpLength)
        self.ConnectionWidth = float(obj.ConnectionWidth)
        self.Sections = int(obj.Sections)
        self.waveDepth=float(obj.waveDepth)
        self.NetDistance=float(obj.NetDistance)
        #Both distances cannot crosse each other 
        if self.BottomDistance == self.TopDistance or self.BottomDistance > self.TopDistance:
            self.BottomDistance = self.TopDistance -(1.0)
            obj.BottomDistance=self.BottomDistance

        elif self.TopDistance < self.BottomDistance:
            self.TopDistance = self.BottomDistance + (1.0)
            obj.TopDistance=self.TopDistance
        obj.Shape = self.createObject()

class Design456_Fence:
    def GetResources(self):
        return {'Pixmap': Design456Init.ICON_PATH + 'Fence.svg',
                'MenuText': "Fence",
                'ToolTip': "Generate a Fence"}

    def Activated(self):
        newObj = App.ActiveDocument.addObject(
            "Part::FeaturePython", "Fence")
        plc = App.Placement()
        plc.Base = App.Vector(0, 0, 0)
        plc.Rotation.Q = (0.0, 0.0, 0.0, 1.0)
        newObj.Placement = plc

        BaseFence(newObj)
        ViewProviderFence(newObj.ViewObject, "Fence")
        v = Gui.ActiveDocument.ActiveView
        App.ActiveDocument.recompute()
        faced.PartMover(v, newObj, deleteOnEscape=True)

Gui.addCommand('Design456_Fence', Design456_Fence())