import unittest
from package.clazz import SampleClass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = SampleClass("Hello")
        self.assertEqual(c.write(), "Hello")


if __name__ == '__main__':
    unittest.main()
