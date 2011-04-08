#Copyright (c) 2011 Thomas Scrace <tom@scrace.org>

#This program is free software; you can redistribute it and/or modify
#it under the terms of Version 2 of the GNU General Public License as published
#by the Free Software Foundation.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""Encipher text using a Caesar-type cipher."""

import caesar
import sys
import getopt
from types import *

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    if len(args) > 0:
        source = args[0]
        if len(args) > 1:
            destination = args[1]
    else:
        usage()
        sys.exit()
    key = False
    while not key:
        k = raw_input("Enter the key to use for encryption. If you do not enter a key, one will be chosen for you at random.")
        if k == '':
            key = None
            break
        if type(int(k)) == IntType and (0 <= int(k) <= 25):
            key = int(k)
        else:
            print "Invalid input."

    plain = load_file(source)
    if not plain:
        plain = source

    if plain:
        cipher = caesar.encipher(plain, key)
    else:
        die("Could not determine source.")
    if not cipher:
        die("Could not encipher.")
    if destination:
        save_to_file(destination, cipher)
    else:
        print cipher

def load_file(file_name):
    contents = ''
    try:
        f = open(file_name)
        try:
            for l in f:
                contents += l
        finally:
            f.close()
    except IOError:
        return False
    return contents

def save_to_file(file_name, contents):
    try:
        f = open(file_name, 'w')
        try:
            f.write(contents)
        finally:
            f.close()
    except IOError:
        die("Error writing to file.")
    return

def usage():
    usage = open('usage.txt')
    for l in usage:
        print l,
    usage.close()

def die(message):
    print message
    sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])