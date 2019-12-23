#Unit tests
import unittest
import DonorAI as ai

class TestCSVParsing(unittest.TestCase):

    def test_example_file_one(self):
        data_set = ai.parse_csv('example.csv')
        self.assertEqual(data_set[2]['priority'], '1/2/2014')
        self.assertEqual(data_set[3]['priority'], '1/3/2014')
        self.assertEqual(data_set[4]['priority'], '1/4/2014')

if __name__ == '__main__':
    unittest.main()