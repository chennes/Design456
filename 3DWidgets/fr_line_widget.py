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

"""
This class is the base class for all widgets created in coin3D

"""
import os,sys
import FreeCAD  as App
import FreeCADGui as Gui
import pivy.coin as coin
import Design456Init
import Draft as _draft
import fr_draw 
import fr_widget
import constant



class Fr_Line_Widget(fr_widget.Fr_Widget):
    selfwidget=None
    def __init__(self, x,y,z,w,h,t,l=""):
      super().__init__(x,y,z,h,w,t,l)
      
    def handel(self, event):
        if event==const.Events.MOUSE_LEFT_CLICK:
            self.setFocus(self)
    def draw(self):
        p1=(self.x,self.y,self.z)
        p2=(self.x+self.w,self.y+self.h,self.z+self.t)
        self.color1= constant.FR_COLOR.FR_Green
        self.color2= constant.FR_COLOR.FR_Yellow  #Focus
        LineWidth=4
        if self.hasFocus:
            selfwidget=fr_draw.draw_line(p1, p2, self.color1, LineWidth)
        else:
            selfwidget=fr_draw.draw_line(p1, p2, self.color2, LineWidth)
        self.parent.addSeneNode(selfwidget)
    
    def redraw(self):
        parent(self).removeSeneNode(selfwidget)
        selfwidget=None
        self.draw()