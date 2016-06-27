#!/usr/bin/env python

import unittest
from FinalImplementation import *

class finalTest(unittest.TestCase):
    def testTests(self):
        self.assertTrue(True, "Error: Something is wrong with your tests")
    def testfillQuestionListBasic(self):
        test=fillQuestionListBasic()
        self.assertEqual(test,1, "Error: Did not fill basic questions correctly")
    def testfillAnswerListBasic(self):
        test=fillAnswerListBasic()
        self.assertEqual(test,1,"Error: Did not fill basic answers correctly")
    def testfillQuestionListDifficulty(self):
        test=fillQuestionListDifficulty('Hard')
        self.assertEqual(test,1,"Error: Did not fill hard questions correctly")
    def testfillQuestionListDififcultyMedium(self):
        test=fillQuestionListDifficulty("Medium")
        self.assertEqual(test,1,"Error:Did not fill medium questions correctly")
    def testbadfillQUestionListDifficulty(self):
        test=fillQuestionListDifficulty("Bad string")
        self.assertEqual(test,0,"Error: Did not handle bad string correctly")
    def testfillAnswerListDifficulty(self):
        test=fillAnswerListDifficulty("Hard")
        self.assertEqual(test,1,"Error: Did not fill hard answers correctly")
    def testfillAnswerListDifficultyMedium(self):
        test=fillAnswerListDifficulty("Medium")
        self.assertEqual(test,1,"Error: Did not fill medium answers correctly")
    def testbadfillAnswerListDifficulty(self):
        test=fillAnswerListDifficulty("Bad string")
        self.assertEqual(test,0,"Error: Did not handle bad string correctly")


if __name__ == '__main__':
    unittest.main()
