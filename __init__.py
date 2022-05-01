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

def changeGlobalFontSize(font_size):
    font = QApplication.font()
    font.setPixelSize(font_size)
    QApplication.setFont(font)

def changeWebFontSize(font_size):
	try:
		# Qt6
		wes = QWebEngineProfile.defaultProfile().settings()
	except AttributeError:
		# Qt5
		wes = QWebEngineSettings.globalSettings()
	
	#wes.setFontSize(QWebEngineSettings.DefaultFontSize, font_size)
	wes.setFontSize(QWebEngineSettings.MinimumFontSize, font_size)

def changeFontSize(config):
    font_size = config['font_size']
    changeGlobalFontSize(font_size)
    changeWebFontSize(font_size)

changeFontSize(mw.addonManager.getConfig(__name__))

mw.addonManager.setConfigUpdatedAction(__name__, changeFontSize)
