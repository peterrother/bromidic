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

import datetime
import os
import sys
import cgi
from datetime import date

from textile import Textile

from config import *
from filehelper import writefile


class Entry:
    """Entry is the object representing a blog entry"""


    def __init__(self, filepath, template):
        """Class construction"""
        self.filepath = filepath
        self.template = template

        self._tt = Textile()

        self._parse_file_contents()
        self._parse_file_path()

        # Map parsed information to template
        self._templatize()

    def _templatize(self):
        d = date.today()
        current = d.strftime("%Y-%m-%dT%H:%M:%S%z") 

        mappings = ({
            '{{ BODY }}': self.htmlbody,
            '{{ ESCBODY }}': cgi.escape(self.htmlbody),
            '{{ TITLE }}': self.title,
            '{{ URL }}': self.relative_url,
            '{{ DATE }}': self.prettydate,
            '{{ HOMEURL }}': URL,
            '{{ DATESTAMP }}': current[:-2] + ':' + current[-2:],
            '{{ TAG }}': d.strftime('%Y-%m-%d') + ':' + self.relative_url,
            '{{ PUBLISHED }}': self.year + '-' + self.month + '-' + self.day,
        })

        filehandle = open(self.template)
        contents = filehandle.read()

        for key in mappings:
            contents = contents.replace(key, mappings[key])
        self.template_contents = contents

    def _parse_file_contents(self):
        filehandle = open(self.filepath)
        self.title = filehandle.readline().split('Title: ')[1].strip()
        filehandle.seek(0)
        body = self._tt.textile(filehandle.read())
        body = body.split(self.title + '</p>')[1].strip()
        self.htmlbody = body[0:]

    def _parse_file_path(self):
        entry_dir = self.filepath.split(PWD)[1].split("/")[0] + "/"
        parts = self.filepath.split(entry_dir)[1].split("/")

        self.relative_url = "/"
        self.prettydate = ""
        self.year = ""
        self.month = ""
        self.day = ""
        self.filename = parts[len(parts)-1].split(".textile")[0]

        if entry_dir == "entries/":
            self.year = parts[0]
            self.month = parts[1]
            self.day = parts[2]

            date = datetime.date(int(self.year),
                                 int(self.month),
                                 int(self.day))

            self.prettydate = date.strftime("%e %B %Y")
            self.relative_url = os.path.join(self.relative_url,
                                             self.year,
                                             self.month,
                                             self.day)

        self.relative_url = os.path.join(self.relative_url,
                                         self.filename) + ".html"

    def _createdir(self):
        outdir = WWWDIR
        if self.year != "" and self.month != "" and self.day != "":
            outdir = os.path.join(WWWDIR, self.year, self.month, self.day)
        if not os.path.isdir(outdir):
            os.makedirs(outdir)

    def _createfile(self):
        outfile = WWWDIR
        if self.year != "" and self.month != "" and self.day != "":
            outfile = os.path.join(outfile, self.year, self.month, self.day)
        outfile = outfile + "/" + self.filename + ".html"
        writefile(outfile, self.template_contents)

    def publish(self, filepath=""):
        """Saves the entry to webroot"""
        if filepath != "":
            writefile(filepath, self.template_contents)
        else:
            self._createdir()
            self._createfile()

