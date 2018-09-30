# -*- coding: utf-8 -*-

# Copyright (C) 2018  Christopher James Howard
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from aqt import mw
from aqt.qt import *

config = mw.addonManager.getConfig(__name__)
font_size = config['font_size']

def changeGlobalFontSize():
    font = QApplication.font()
    font.setPixelSize(font_size)
    QApplication.setFont(font)

def changeWebFontSize():
    wes = QWebEngineSettings.globalSettings()
    #wes.setFontSize(QWebEngineSettings.DefaultFontSize, font_size)
    wes.setFontSize(QWebEngineSettings.MinimumFontSize, font_size)

def changeFontSize():
    changeGlobalFontSize()
    changeWebFontSize()

changeFontSize()
