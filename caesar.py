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

"""Encipher and decipher text using a simple Caesar shift cipher.

Some functions to allow for encipherment and decipherment of text using a simple Caesar-type substitution cipher. Simply use the encipher and decipher functions to perform these opertions. Each function takes two arguments: the text to be translated, and a substitution key which determines how many letters to jump. If no key is for encipherment a random key will be used. If no key is provided for decipherment, decipher() will attempt to find the key.

Example:

>>> cipher = caesar.encipher('Hello, world!', 10)
>>> cipher
'Rovvy, gybvn!'
>>> plain = caesar.decipher(cipher, 10)
>>> plain
'Hello, world!'

"""

import string
import random

def build_translation_table(offset, operation):
    assert operation in ['de', 'en'], "Operation must be either en or de"

    lwr = string.ascii_lowercase
    upr = string.ascii_uppercase
    new_lwr = new_alpha(lwr, offset)
    new_upr = new_alpha(upr, offset)

    full_alpha = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    new_full_alpha = new_lwr + new_upr + string.digits + string.punctuation + string.whitespace

    if operation == 'en':
        return string.maketrans(full_alpha, new_full_alpha)
    elif operation == 'de':
        return string.maketrans(new_full_alpha, full_alpha)
    else:
        return 0

def new_alpha(alpha, offset):
    new_alpha = ''
    for i in range(len(alpha)):
            new_alpha += alpha[(i + offset) - len(alpha)]
    return new_alpha

def get_words():
    f = open('/usr/share/dict/words', 'r', 0)
    words = []
    for line in f:
        words.append(line.strip().lower())
    return words

def get_cipher_words(cipher):
    cipher_words = []
    word = ''
    for char in cipher:
        if char in string.ascii_letters:
            word += char.lower()
        elif len(word) > 0:
            cipher_words.append(word)
            word = ''
    return cipher_words

def find_key(cipher):
    words = get_words()
    cipher_words = get_cipher_words(cipher)
    flag = 0
    for i in range(26):
        if decipher(cipher_words[0], i)in words and decipher(cipher_words[10], i) in words:
            return i
            #for word in cipher_words[1:]:
                #if decipher(word, i) not in words:
                   # flag = 1
            #if not flag:
                #return i
           # else:
                #flag = 0
                #continue
    return False

def encipher(plain, key=None):
    if key == None:
        keys = range(1, 26)
        random.shuffle(keys)
        key = keys[0]
        print "Will use %d as key" % key
    table = build_translation_table(key, 'en')
    return plain.translate(table)

def decipher(cipher, key=None):
    if key == None:
        key = find_key(cipher)
        if key:
            print "Key is %d" % key
        else:
            print "Key not found."
            return False
    table = build_translation_table(key, 'de')
    return cipher.translate(table)

