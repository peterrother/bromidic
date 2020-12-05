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
import sys

from config import *
from filehelper import copyfiles
from entryfactory import EntryFactory


def main():
    """Controls application flow, duh"""
    print "Reticulating blog entries"
    process_writings(ENTRYDIR, ENTRYTEMPLATE)

    print "Copying static files (css, etc) to webroot"
    copyfiles(STATICDIR, WWWDIR)

    print "Creating the home page"
    create_home(ENTRYDIR, ENTRYTEMPLATE, INDEX)

    print "Generating custom pages"
    process_writings(PAGEDIR, PAGETEMPLATE)

    print "Updating RSS feed"
    update_rss(ENTRYDIR, FEEDTEMPLATE, FEED)

    print "Done"


def create_home(dir, template, filepath):
    """Generates the index page"""
    ef = EntryFactory(template)
    ef.write_last_entry(dir, filepath)


def process_writings(dir, template):
    """Calls a factory method that processes all entries"""
    ef = EntryFactory(template)
    entry_count = ef.write_entries(dir)
    if entry_count == 0:
        print "I couldn't find any files in the dir."
        cont = raw_input("Continue (y/n)?")
        if cont == "n":
            sys.exit(1)


def process_args():
    """Processes CLI arguments used for different program actions"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--rebuild':
            for e in entries:
                e.write()
                print '.',
            print '\nAll entries rebuilt and saved'
        elif sys.argv[1] == '--post':
           print 'post'
        else:
            print '\nUnknown argument'
            sys.exit(-1)
    else:
        lastentry = entries[-1]
        lastentry.write()
        print '\nLast entry saved'


def update_rss(dir, template, filepath):
    ef = EntryFactory(template)
    ef.write_last_entry(dir, filepath)

if __name__ == '__main__':
    main()
