import pandas as pd
import convertFile2Json
import json
import unittest

class TestMain(unittest.TestCase):

    def get_json_by_file(self, input_file):
        c = convertFile2Json.convert()
        out = c.convert(input_file)
        return out

    # test case for a valid input
    def test_for_valid_case(self):

        input_file = "./test1.txt"
        out = self.get_json_by_file(input_file)
        self.assertEqual(len(out['entries']) , 1)

    # test case for an invalid input
    def test_for_invalid_case(self):

        input_file = "./test2.txt"
        out = self.get_json_by_file(input_file)
        self.assertEqual(len(out['entries']) , 0)

if __name__ == '__main__':
    unittest.main()
