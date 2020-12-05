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

# You'll probably want to modify these two lines
PWD = "./"
URL = "http://www.google.com/"

# I wouldn't worry about the ones below

ENTRYDIR = PWD + "entries"
PAGEDIR = PWD + "pages"
STATICDIR = PWD + "static"
WWWDIR = PWD + "www"

ENTRYTEMPLATE = PWD + 'templates/base.html'
PAGETEMPLATE = PWD + 'templates/page.html'
FEEDTEMPLATE = PWD + 'templates/atom.xml'

INDEX = WWWDIR + '/index.html'
FEED = WWWDIR + '/index.xml'

