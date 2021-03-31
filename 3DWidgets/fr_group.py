
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
import FreeCAD  as App
import FreeCADGui as Gui
import pivy.coin as coin
import Design456Init
import Draft as _draft
import fr_widget 
import constant 

#Group class. Use this to collect several widgets.
class Fr_Group(fr_widget.Fr_Widget):
    #Any drawign/Every thing should be added to this later 
    global Root_SeneGraph  
    global children
    def __init__(self, x,y,z,h,w,t,l):
        self.WidgetType=constant.FR_WidgetType.FR_GROUP
        self.Root_SeneGraph = Gui.ActiveDocument.ActiveView.getSceneGraph()
        self.children=[]
        self.MainCoinNode=self.Root_SeneGraph # Main and 
        super().__init__(x,y,z,h,w,t,l)
        
    def addWidget(self,widget):
        self.children.append(widget)
        
    def draw(self):
        for i in self.children:
            i.draw()
    def draw_label(self):
        for i in self.children:
           i.draw_label() 
    
    def redraw(self):
        for i in self.children:
            i.draw(self)

    def deactivate(self):
        for widget in self.children:
            del widget
        self.children.clear()

    def addSeneNode(self, sen):
        self.Root_SeneGraph.addChild(sen)  #add sen to the root
        self.wdgsoSwitch.addChild(sen)  #add switch also
        
    def removeSeneNode(self, sen):
        self.Root_SeneGraph.removeChild(sen)

        

    def handle(self,events):
        """send events to all widgets
        Targeted Widget should return 1 if it uses the event 
        Sometimes there might be several widgets that need to get the event, 
        at that time return the event to achieve that. 
        To find the target widget, you have to 
        calculate find  the clicked object related to the mouse position.
        Widgets shouldn't get the event if they are not targeted to not 
        waste cpu:s time.     
        
        """
        for widg in self.children:
            if widg.handle(events) == 1:
                #Events reached the targeted widget go out
                return 1
 