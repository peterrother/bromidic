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

from entry import Entry

class EntryFactory:
    """Awesome class"""

    def __init__(self, template):
        self.template = template

    def write_entries(self, dir):
        """Traverses through given directory and locates all .textile
           files, then adds each of them to an Entry object and
           writes all entries.
        """
        entries = self._get_entries(dir)
        count = len(entries)
        for e in entries:
            e.publish()
        return count

    def write_last_entry(self, dir, filepath=""):
        entries = self._get_entries(dir)
        lastentry = entries[-1]
        lastentry.publish(filepath)

    def _get_entries(self, dir):
        entries = []
        for root, dirs, files in os.walk(dir):
            if len(files) > 0:
                for file in os.listdir(root):
                    if file.endswith(".textile"):
                        entries.append(Entry(root + "/" + file,
                                             self.template))
        return entries
       
