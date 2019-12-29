#Unit tests

#Python imports.
#Part of the Python base modules.
import unittest, csv, random

#Non-base modules.
import DonorAI as ai
import Parsing as pa
import Communications
import pprint
from webbot import Browser

class TestCSVParsing(unittest.TestCase):

    """
    Test class for checking that CSV data parsing works properly.
    """
    def get_CSV_Reader(self, file_name):
        
        """
        Return a tuple of an open csv_file
        and csv.reade object

        file_name - Name of the file to opened.
        """
        csv_file = open(file_name)
        readCSV = csv.reader(csv_file, delimiter=',')
        return (csv_file, readCSV)

    def check_random_row(self, file_name):

        """
        Check if all the values in a random row in the csv file
        are equivalent to it's corresponding entry in the date_set dict.

        file_name - Name of the file to be checked.
        """
        data_set = pa.DataParser().parse_csv(file_name)
        test_tup = self.get_CSV_Reader(file_name)
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
    
    #Run the same test 5 times with different files.
    def test_example_file_one(self):
        self.check_random_row('volunteer_sample_1.csv')
    def test_example_file_two(self):
        self.check_random_row('volunteer_sample_2.csv')
    def test_example_file_three(self):
        self.check_random_row('volunteer_sample_3.csv')
    def test_example_file_four(self):
        self.check_random_row('volunteer_sample_4.csv')
    def test_example_file_five(self):
        self.check_random_row('volunteer_sample_5.csv')

class TestURLConnection(unittest.TestCase):

    """
    Test class for checking that connecting to a url and getting
    a cookie works properly.
    """

    def test_van(self):
        data_set = pa.DataParser().parse_csv('volunteer_sample_2.csv')
        comm = Browser(showWindow=True)
        mappings = {
            'FirstName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterFirstName',
            'LastName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterLastName',
            'City': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterCity_DropDownListCity',
            'Cell': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterPhone',
            'StreetAddress': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'StreetAddress_2': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'Zip': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterZip',
            'Email': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterEmail_FilterEmail'
        }
        web_comm = Communications.WebComm(mappings)
        web_comm.login_van(comm, 'Slark1101', 'tschaffner23@gmail.com')
        result = web_comm.simple_search(comm, 'https://www.texasvan.com/QuickLookUp.aspx', ['StreetAddress', 'StreetAddress_2','City'], data_set[2])
        self.assertEqual('https://www.texasvan.com/ContactsDetails.aspx?VANID=EIDFA1F7B1F', result)

if __name__ == '__main__':
    unittest.main()


    #ctl00_ContentPlaceHolderVANPage_ctl32_ctl00_ContentPlaceHolderVANPage_ctl32_ctl00Panel
    #ctl00_ContentPlaceHolderVANPage_ctl32_ctl00_ContentPlaceHolderVANPage_ctl32_ctl00Panel