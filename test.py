import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 61)
   def test_from_ndarray():

#"""See issue 7465."""
#try:
#from numpy import array
#except ImportError:
#skip('NumPy must be available to test creating matrices from ndarrays')


def main():
    unittest.main()

if __name__ == "__main__":
    main()
