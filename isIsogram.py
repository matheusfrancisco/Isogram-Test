from unittest import TestCase, main


class Isogram:
    def isIsogram(self, word):
        if not isinstance(word, str):
            raise TypeError('Argument  invalid, should be a string')
        if not word:
            isogram = False
        else:
            isogram = len(word) == len(set(word.lower()))
        return isogram



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

    ''' Por mais que seja uma palavra muito grande ele vai ter que
    verificar o tamanho do alfabeto + numeros + caracteres especial
    isso não vai travar um programa em python no set() '''
    def testWithBigWords(self):
        self.assertEqual(self.isogram.isIsogram("abcdefghijklmnopqrstuvwxyz.,;:><1234567890"), True)


    def testCaseInsensitive(self):
        self.assertEqual(self.isogram.isIsogram("TEST"),False)


if __name__== "__main__":
    main()
