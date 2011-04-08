#Copyright (c) 2011 Thomas Scrace <tom@scrace.org>

#This program is free software; you can redistribute it and/or modify
#it under the terms of version 2 of the GNU General Public License as published
#by the Free Software Foundation.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""Test the caesar module."""

import string
import caesar
import random

def test_1():
    """Test every three-character-long combination of printables for every 4th key. Return True if success, False if failure.

    """
    for word in [a + b + c for a in string.printable for b in string.printable for c in string.printable]:
        for i in range(0, 26, 4):
            if caesar.decipher(caesar.encipher(word, i), i) != word:
                print "TEST 1 FAILED"
                return False
    print "TEST 1 SUCCEEDED"
    return True

def test_2():
    """Test a long random string.  Return True if success, False if failure."""
    long_string = ''
    numbers = range(100)
    random.shuffle(numbers)
    j = 0
    for i in range(100001):
        if j == 99:
            random.shuffle(numbers)
            j = 0
        long_string += string.printable[numbers[0]]
        j += 1
    for i in range(26):
        if caesar.decipher(caesar.encipher(long_string, i), i) == long_string:
            print "TEST 2 SUCCEEDED"
            return True
    print "TEST 2 FAILED"
    return False

def test_3():
    """Test random key encipherment, and unknown key decipherment."""
    words = caesar.get_words()
    random.shuffle(words)
    plain = ''
    for i in range(100):
        plain += words[i]
        plain += ' '
    if caesar.decipher(caesar.encipher(plain)) != plain:
        print "TEST 3 FAILED"
        return False
    print "TEST 3 SUCCEEDED"
    return True

def test_suite():
    print "Testing...."
    if not test_1():
        return False
    elif not test_2():
        return False
    elif not test_3():
        return False
    return "ALL TESTS SUCCEEDED"

if __name__ == "__main__":
    print test_suite()



