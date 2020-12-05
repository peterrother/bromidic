"""
Copyright (c) 2009-2011 Peter Rother. All rights reserved.

This file is part of bromidic.

bromidic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

bromidic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with bromidic.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import shutil
import sys


def writefile(filepath, contents):
	filehandle = open(filepath, 'w')
	filehandle.write(contents)
	filehandle.close()


def copyfiles(src, dst):
    names = os.listdir(src)
    if not os.path.isdir(dst):
        os.makedirs(dst)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        shutil.copy2(srcname, dstname)
	
