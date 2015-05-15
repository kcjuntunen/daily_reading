#!/bin/env python

import unittest
import daily_reading

class TestMethods(unittest.TestCase):
    def test_list(self):
        dr = daily_reading.DailyReading("biay.json")
        x = dr.get_passages()
        print("".join(x))

    def test_print(self):
        dr = daily_reading.DailyReading("mcheyne.json")
        dr.print_passages()

    def test_err(self):
        dr = daily_reading.DailyReading("asfd.json")

if __name__ == "__main__":
    unittest.main()
