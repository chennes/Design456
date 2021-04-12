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

import os, sys
import FreeCAD as App
import FreeCADGui as Gui
import Design456Init

from nurbs import *



class Design456_Nurbs_2DToolsGroup:
    
    """Design456 Part 2D Drawing"""

    def GetCommands(self):
        import nurbs
        """3D Modifying Tools."""
        return ("TopologicalAnalyse",
                "addToVertexStore",
                "TopologicalCompare",
                "displayVertexStoreCommonPoints",
                "displayQualityPoints",
                "printGraphData",
                "printDATA",
                "resetVertexStore",
                "printVertexStore",
                "map3Dto2D",
                "map2Dto3D",
                "map3Dgridto2Dgrid",
                "'createBrezel"
                


                )

    def GetResources(self):
        import Design456Init
        from PySide.QtCore import QT_TRANSLATE_NOOP
        """Set icon, menu and tooltip."""
        _tooltip = ("Different Tools - Nurbs")
        return {'Pixmap':  Design456Init.NURBS_ICON_PATH + 'Nurbs2.svg',
                'MenuText': QT_TRANSLATE_NOOP("Design456", "NurbsTools"),
                'ToolTip': QT_TRANSLATE_NOOP("Design456", _tooltip)}

Gui.addCommand("Design456_Nurbs_2DToolsGroup", Design456_Nurbs_2DToolsGroup())