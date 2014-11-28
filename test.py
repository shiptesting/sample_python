import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 61)
    def test_from_ndarray(self):
    app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)
skip('NumPy must be available to test creating matrices from ndarrays')


def main():
    unittest.main()

if __name__ == "__main__":
    main()
