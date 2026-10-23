import unittest

class TestApp(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(200, 200)

if __name__ == "__main__":
    unittest.main()