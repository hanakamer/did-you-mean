import unittest
from main import edit_distance
from main import min_edit_distance

class TestMain(unittest.TestCase):
    def test_ed_dif(self):
        res = edit_distance('abcdef', 'azced')
        self.assertEqual(res,3)

    def test_ed_equal(self):
        res = edit_distance('abc', 'abc')
        self.assertEqual(res,0)

    def test_ed_one(self):
        res = edit_distance('', 'abcd')
        self.assertEqual(res,4)

    def test_med_(self):
        res =min_edit_distance('burak')
        self.assertEqual(res,'bura')

    def test_med_capital(self):
        res =min_edit_distance('MASA')
        self.assertEqual(res,'masa')

    def test_med_mixed_case(self):
        res =min_edit_distance('Masa')
        self.assertEqual(res,'masa')

if __name__ =='__main__':
    unittest.main()
