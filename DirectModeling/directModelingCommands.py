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
from DirectModeling.smartscale import *
class Design456_DirectModeling:
    list = ["Design456_SmartScale",
            "Design456_DirectScale",

            ]
    """Design456 Direct Modeling """

    def GetResources(self):
        import Design456Init
        return{
            'Pixmap':    Design456Init.ICON_PATH + 'DirectModeling.svg',
            'MenuText': 'Direct Modeling Tools',
            'ToolTip':  'Direct Modeling Tools'
        }

    def Activated(self):
        self.appendToolbar("Design456_DirectModeling", self.list)