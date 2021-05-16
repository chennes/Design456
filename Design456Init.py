# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
# ***************************************************************************
# *                                                                         *
# *  This file is a apart of the Open Source Design456 Workbench - FreeCAD. *
# *                                                                         *
# *  Copyright (C) 2021                                                     *
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
# *  Author : Mariwan Jalal   mariwan.jalal@gmail.com                       *
# ***************************************************************************
import os,sys
import FreeCAD as App
from draftutils.translate import translate   #for translate
"""
This file will add all paths needed for the Design456.
It makes life easier. By doing that you can import any file
in any of the subdirectories. Adding more subdirectories
needs be added here. 
ICON path should be always added as bellow 
'Resources/icons/' 

"""
#Design456 
__dir__ = os.path.dirname(__file__)
ICON_PATH = os.path.join(__dir__, 'Resources/icons/')
IMAGE_PATH = os.path.join(__dir__, 'Resources/images/')
#Pyramid shapes 
PYRAMID_PATH = os.path.join(__dir__, 'PyramidMo/')
PYRAMID_ICON_PATH = os.path.join(__dir__, 'PyramidMo/Resources/icons/')

#Coin3D New widget system 
WIDGETS3D_PATH=os.path.join(__dir__,'ThreeDWidgets/')

#Direct Modeling implementation 
WIDGETS3D_PATH=os.path.join(__dir__,'DirectModeling/')

# PART
App.addImportType("BREP format (*.brep *.brp)", "Part")
App.addExportType("BREP format (*.brep *.brp)", "Part")
App.addImportType("IGES format (*.iges *.igs)", "Part")
App.addExportType("IGES format (*.iges *.igs)", "Part")
App.addImportType("STEP with colors (*.step *.stp)", "Import")
App.addExportType("STEP with colors (*.step *.stp)", "Import")

#Desing456 WB Default  view 
#Default Extrusion direction, i.e. 2D/3D objects are placed on XY plane by default.
DefaultDirectionOfExtrusion='z' # We need to know this always. Any change in the plane should be saved here.

App.__unit_test__ += ["TestPartApp"]
