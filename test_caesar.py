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
from types import *

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

def test_4():
    """Test construction of translation tables"""
    alpha = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25}
    reverse = []
    for char in alpha.keys():
        reverse.append(char)
    reverse.sort()

    for i in range(26):
        for op in ['de', 'en']:
            table = caesar.build_translation_table(i, op)
            for char in string.ascii_letters:
                trans_char = char.translate(table)
                if op == 'en':
                    if dist_between(char, trans_char) != i:
                        print "TEST 4 FAILED"
                        return False
                elif op == 'de':
                    if dist_between(char, trans_char, '-') != i:
                        print "TEST 4 FAILED"
                        return False
            for char in string.digits + string.punctuation + string.whitespace:
                trans_char = char.translate(table)
                if trans_char != char:
                        print "TEST 4 FAILED"
                        return False
    print "TEST 4 SUCCEEDED"
    return True

def dist_between(char_1, char_2, direction='+'):
    """Return the distance between two characters in an infinitely looped (a follows z) alphabet when travelling in a given direction. If no direction is supplied, assume forwards.

    char_1, char_1 must be in string.ascii_letters
    direction should be '-' if backwards

    """
    assert char_1 in string.ascii_letters, "char_1 must be a letter"
    assert char_1 in string.ascii_letters, "char_1 must be a letter"
    assert direction in ['+', '-'], "direction must be either '-' or '+'"

    char_1 = char_1.lower()
    char_2 = char_2.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                            'k', 'l', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x',
                            'y', 'z']
    if direction == '-':
        alpha.reverse()
    mark = False
    finished = False
    while not finished:
        for letter in alpha:
            if type(mark) == IntType:
                mark += 1
                if letter == char_2:
                    finished = True
                    break
            if letter == char_1:
                mark = 0
                if letter == char_2:
                    finished = True
                    break
    return mark

def test_suite():
    print "Testing...."
    if not test_1():
        return False
    elif not test_2():
        return False
    elif not test_3():
        return False
    elif not test_4():
        return False
    return "ALL TESTS SUCCEEDED"

if __name__ == "__main__":
    print test_suite()



