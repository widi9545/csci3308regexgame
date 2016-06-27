#!/usr/bin/env python


import unittest
from memorygame import *

class MemorygameTestCase(unittest.TestCase):

    def testFail(self):
        self.assertTrue(False, "Testing to make sure tests fail")
    def testTrue(self):
        self.assertTrue(True)
    def testFindQuestionQID(self):
        test=findQID('End of string')
        actualID=41
        self.assertEqual(test, actualID, "Error in checking question id") 
    def testFindAnswerQID(self):
        test=findQID('*')
        actualID=32
        self.assertEqual(test, actualID, "Error in checking answer id")
    def testNotFindQID(self):
        test=findQID('I am not in the database')
        actualID=None
        self.assertEqual(test, actualID, "Error if bad string is passed in")
        

if __name__ == '__main__':
    unittest.main()

