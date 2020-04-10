# -*- coding: UTF-8 -*-

#########################################################
# Name: opendir.py
# Porpose: open file browser on given pathname
# Compatibility: Python3 (Unix, Windows)
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2018/2020 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev: April.06.2020 *PEP8 compatible*
#########################################################

# This file is part of Videomass.

#    Videomass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Videomass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Videomass.  If not, see <http://www.gnu.org/licenses/>.

#########################################################
import subprocess
import os


def browse(OS, pathname, mod):
    """
    open file browser in a specific location with
    file manager of the OS
    """
    if mod != 'dirconf':
        pathname = os.path.join(pathname, "log")  # normalize os pathname

    if OS == 'Windows':
        cmd = ['cmd', '/c', 'start', pathname]

    elif OS == 'Darwin':
        cmd = ['start', pathname]

    else:  # xdg-open *should* be supported by recent Gnome, KDE, Xfce
        cmd = ['xdg-open', pathname]

    try:
        p = subprocess.run(cmd, capture_output=True)
        if p.stderr:
            return(p.stderr.decode())
    except FileNotFoundError as err:
        return('%s' % (err))
