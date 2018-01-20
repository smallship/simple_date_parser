# coding=utf-8
import unittest
import datetime

from parse_date import parse_date

""" Basic date string parsing tests  """


class TestCase(unittest.TestCase):
    def test_separators(self):
        self.assertEqual(parse_date("19-04-2017"), [datetime.date(2017, 4, 19)])
        self.assertEqual(parse_date("19.04.2017"), [datetime.date(2017, 4, 19)])
        self.assertEqual(parse_date("19/04/2017"), [datetime.date(2017, 4, 19)])
        self.assertEqual(parse_date("19 04 2017"), [datetime.date(2017, 4, 19)])

    def test_unambiguous_dd_mm_yyyy(self):
        self.assertEqual(parse_date("28-12-1962"), [datetime.date(1962, 12, 28)])
        self.assertEqual(parse_date("28-12-0062"), [datetime.date(62, 12, 28)])

    def test_unambiguous__mm_dd_yyyy(self):
        self.assertEqual(parse_date("03-15-1753"), [datetime.date(1753, 3, 15)])
        self.assertEqual(parse_date("3-15-1753"), [datetime.date(1753, 3, 15)])
        self.assertEqual(parse_date("3-15-0053"), [datetime.date(53, 3, 15)])

    def test_ambiguous_nn_nn_yyyy(self):
        date1 = datetime.date(2078, 7, 8)
        date2 = datetime.date(2078, 8, 7)
        self.assertEqual(parse_date("07-08-2078"), [date1, date2])
        self.assertEqual(parse_date("7-8-2078"), [date1, date2])
        date3 = datetime.date(78, 7, 8)
        date4 = datetime.date(78, 8, 7)
        self.assertEqual(parse_date("7-8-0078"), [date3, date4])

    def test_yyyy_mm_dd(self):
        self.assertEqual(parse_date("1066-04-01"), [datetime.date(1066, 4, 1)])
        self.assertEqual(parse_date("0066-04-01"), [datetime.date(66, 4, 1)])

    # yyyy_dd_mm case and thus yyyy_nn_nn ambiguity won't be considered until an real example is found

    def test_unambiguous_dd_mm_yy(self):
        date1 = datetime.date(34, 2, 20)
        date2 = datetime.date(1934, 2, 20)
        date3 = datetime.date(2034, 2, 20)
        self.assertEqual(parse_date("20-02-34"), [date1, date2, date3])

    def test_unambiguous_mm_dd_yy(self):
        date1 = datetime.date(86, 12, 27)
        date2 = datetime.date(1986, 12, 27)
        date3 = datetime.date(2086, 12, 27)
        self.assertEqual(parse_date("12-27-86"), [date1, date2, date3])

    def test_ambiguous_nn_nn_yy(self):
        date1 = datetime.date(40, 11, 12)
        date2 = datetime.date(40, 12, 11)
        date3 = datetime.date(1940, 11, 12)
        date4 = datetime.date(1940, 12, 11)
        date5 = datetime.date(2040, 11, 12)
        date6 = datetime.date(2040, 12, 11)
        self.assertEqual(parse_date("11-12-40"), [date1, date2, date3, date4, date5, date6])

    # def test_unambiguous_yy_mm_dd(self):
    # this case removed until a real example is found
    #     date1 = datetime.date(35, 2, 15)
    #     date2 = datetime.date(1935, 2, 15)
    #     date3 = datetime.date(2035, 2, 15)
    #     self.assertEqual(parse_date("35-2-15"), {date1, date2, date3})

        # yy_dd_mm case and thus yy_nn_nn ambiguity and thus nn_nn_nn ambiguity won't be considered until an real
        # example is found


if __name__ == '__main__':
    unittest.main()