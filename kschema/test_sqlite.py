import unittest
import sqlite as s


class SqliteTest(unittest.TestCase):
    def setUp(self):
        self.dtype = s.Sqlite(89.55)

    def test_returntype(self):
        self.dtype.returntype()
        # self.assertTrue(isinstance(1, int))


if __name__ == '__main__':
    unittest.main()
