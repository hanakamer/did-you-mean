import unittest
from main import editDistance
from main import minEditDistance

class TestMain(unittest.TestCase):
    def test_ed_dif(self):
        res = editDistance('abcdef', 'azced')
        self.assertEqual(res,3)

    def test_ed_equal(self):
        res = editDistance('abc', 'abc')
        self.assertEqual(res,0)

    def test_ed_one(self):
        res = editDistance('', 'abcd')
        self.assertEqual(res,4)

    def test_med_(self):
        res =minEditDistance('burak')
        self.assertEqual(res,'bura')

if __name__ =='__main__':
    unittest.main()
