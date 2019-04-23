#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
import sys

class Isogram:
    def isIsogram(self, word):
        if not isinstance(word, str):
            raise TypeError('Argument  invalid, should be a string')
        if not word:
            isogram = False
        else:
            if(sys.version_info >= (3,0)):
                digit = list(filter(str.isdigit,word))
                if(len(digit) == len([])):

                    isogram = len(word) == len(set(word.lower()))
                    return isogram
                else:
                    return False
            else:
                digit = lambda x: filter(str.isdigit, x)

                if(len(digit(word))==len([])):
                    isogram = len(word) == len(set(word.lower()))
                    return isogram

                else:
                    return False



class TestIsogram(TestCase):
    def setUp(self):
        self.isogram = Isogram()


    def testFalseIsogram(self):
        self.assertEqual(self.isogram.isIsogram("maaa"),False)


    def testTrueIsogram(self):
        self.assertEqual(self.isogram.isIsogram("joan"), True)


    def testWithNumbers(self):
        with self.assertRaises(Exception):
            self.isogram.isIsogram(123)


    def testWithBigWords(self):
        self.assertEqual(self.isogram.isIsogram("abcdefghijklmnopqrstuvwxyz.,;:><"), True)


    def testCaseInsensitive(self):
        self.assertEqual(self.isogram.isIsogram("TEST"),False)


    def testStringWithNumber(self):
        self.assertEqual(self.isogram.isIsogram("123abc"),False)


    def test1(self):
        self.assertEqual(self.isogram.isIsogram("Dermatoglyphics"), True)


    def test2(self):
        self.assertEqual(self.isogram.isIsogram("aba"), False)


    def test3(self):
        self.assertEqual(self.isogram.isIsogram("mo0se"), False)



if __name__== "__main__":
    main()
