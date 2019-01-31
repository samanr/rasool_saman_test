import unittest
from src import QuestionA,QuestionB

class MyTest(unittest.TestCase):
    def test_isCompare(self):
        self.assertEqual(QuestionA.isOverlap([1, 5], [6, 8]), 'Not Overlap')
        self.assertEqual(QuestionA.isOverlap([1, 5], [4, 8]), 'Overlap')
        self.assertEqual(QuestionA.isOverlap([1, 5], [-1, -5]), 'Not Overlap')
        self.assertEqual(QuestionA.isOverlap([1, 5], [0, 2]), 'Overlap')
        self.assertEqual(QuestionA.isOverlap([1, 5], [-1, 0]), 'Not Overlap')
        self.assertEqual(QuestionA.isOverlap([5, -1], [0, -1]), 'Not Overlap')
        self.assertEqual(QuestionA.isOverlap([0, 1], [0, 1]), 'Overlap')


    def test_compareVersion(self):
        self.assertEqual(QuestionB.compareVersion("1", "1"), "both are equal")
        self.assertEqual(QuestionB.compareVersion("2.1", "2.2"), '2.2 is greater')
        self.assertEqual(QuestionB.compareVersion("3.0.4.10", "3.0.4.2"), '3.0.4.10 is greater')
        self.assertEqual(QuestionB.compareVersion("4.08", "4.08.01"), '4.08.01 is greater')
        self.assertEqual(QuestionB.compareVersion("3.2.1.9.8144", "3.2"), '3.2.1.9.8144 is greater')
        self.assertEqual(QuestionB.compareVersion("3.2", "3.2.1.9.8144"), '3.2.1.9.8144 is greater')
        self.assertEqual(QuestionB.compareVersion("1.2", "2.1"), '2.1 is greater')
        self.assertEqual(QuestionB.compareVersion("2.1", "1.2"), '2.1 is greater')
        self.assertEqual(QuestionB.compareVersion("5.6.7", "5.6.7"), 'both are equal')
        self.assertEqual(QuestionB.compareVersion("1.01.1", "1.1.1"), 'both are equal')


    if __name__ == '__main__':
        unittest.main()