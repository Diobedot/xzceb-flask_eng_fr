import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def testFE1(self):
        #self.assertEqual(french_to_english(''),'')
        pass
    def testFE2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

class TestEnglishToFrench(unittest.TestCase):
    def testEF1(self):
        #self.assertEqual(english_to_french(''),'')
        pass
    def testEF2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

unittest.main()