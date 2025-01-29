import unittest

from python_template import foo

class TestFoo(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(foo.bar(), "bar", "Should be `bar`")

if __name__ == '__main__':
    unittest.main()