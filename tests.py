import unittest
import task


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

if __name__ == '__main__':
    unittest.main()
