import unittest
import task
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())


class CircleAreaTest(unittest.TestCase):

    def test1(self):
        radius = 3
        expected = 28.26
        self.assertEqual(expected, task.circleArea(radius))

    def test2(self):
        radius = 2.5
        expected = 19.625
        self.assertEqual(expected, task.circleArea(radius))


class ListTest(unittest.TestCase):

    def test1(self):
        list = [1, 2, 3, 4]
        expectedFirst = 1
        expepctedLast = 4
        self.assertEqual((expectedFirst, expepctedLast), task.list(list))


class DaysTest(unittest.TestCase):

    def test1(self):
        date1 = date(2011,11,17)
        date2 = date(2011,11,9)
        expected = 8
        self.assertEqual(expected, task.days(date1, date2))

    def test2(self):
        date1 = date(2011,12,12)
        date2 = date(2011,10,2)
        expected = 71
        self.assertEqual(expected, task.days(date1, date2))


if __name__ == '__main__':
    unittest.main()
