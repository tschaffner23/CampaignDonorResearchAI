#Unit tests
import unittest, csv, random
import DonorAI as ai

class TestCSVParsing(unittest.TestCase):

    def get_CSV_Reader(self, file_name):
        
        """
        Return a tuple of an open csv_file
        and csv.reade object

        file_name - Name of the file to opened.
        """
        csv_file = open(file_name)
        readCSV = csv.reader(csv_file, delimiter=',')
        return (csv_file, readCSV)

    def test_example_file_one(self):

        """
        Test if the csv data was parsed correctly by comparing
        a random data_set entry to its csv row.
        """
        data_set = ai.parse_csv('Mann Volunteer Research - Taylor S.csv')
        test_tup = self.get_CSV_Reader('Mann Volunteer Research - Taylor S.csv')
        #Pick a random row and iterate to it.
        row_num = random.randrange(2, 200)
        row = None
        for x in range(row_num):
            row = next(test_tup[1])
        #Check that all of the variables in the csv row are equivalent to those
        #in that row's entry in the data_set dictionary.
        entry = data_set[row_num]
        for col, key in zip(row, entry.keys()):
            self.assertEqual(col, entry[key])
        test_tup[0].close()

if __name__ == '__main__':
    unittest.main()