import unittest
from app import greet

class testApp(unittest.TestCase):
  def test_greet(self):
    self.assertEqual(
      greet(),
      "Hello from python CI/CD app"
    )

if __name__=="__main__":
  unittest.main()
  
