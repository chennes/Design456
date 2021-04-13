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
# * Modified and adapted to Desing456 by:                                  *
# * Author : Mariwan Jalal   mariwan.jalal@gmail.com                       *
# **************************************************************************

# distance between the target curve 1st, and some other curves

import FreeCADGui as Gui
import FreeCAD as App

import os
import Design456Init
try:
    import numpy as np 
except ImportError:
    print ("Trying to Install required module: nump")
    os.system('python -m pip3 install numpy')
import Draft

def  dist(a,b):

    [a,b]=[b,a]
    ptas=a.Shape.Edge1.Curve.discretize(100)
    cb=b.Shape.Edge1.Curve

    pts=[]
    ls=[]
    for pa in ptas:
        pm=cb.parameter(pa)
        v=cb.value(pm)
        ls.append((v-pa).Length**2)
        pts.append(v)

#    Draft.makeWire(pts)
#    Draft.makeWire(ptas)

    ls=np.array(ls)
#    print ls
    ls.min()
    ls.max()
#    print (ls.max(),ls.min(),ls.mean())
    return ls.mean()



def run():
    sel=Gui.Selection.getSelection()
    b=sel[0]
    for a in sel[1:]:
        print (str(a.Label),round(dist(a,b),3))
