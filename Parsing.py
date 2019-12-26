#DataParser used by the AI

#Python imports.
#Part of the Python base modules.
import csv

#data variables initialized for later use.

#Hard coded shell dictionary.
shell = {   'VANID': '',
            'Priority': '', 
            'FirstName': '', 
            'Mid': '',
            'LastName': '', 
            'Suf': '', 
            'StreetAddress': '',
            'StreetAddress_2': '',
            'City': '',
            'State': '',
            'Zip': '',
            'Zip4': '',
            'Country_code': '',
            'Home': '',
            'Cell': '',
            'Work': '',
            'Email': '',
            'Notes': '',
            'Occupation': '',
            'Employer': ''
            }

class DataParser():

    """
    Class that parses data from both web pages and csv files.
    """

    #Method for parsing our csv files given a file name.
    def parse_csv(self, file_name):

        """
        Parse out all of the data in a csv file into a dictionary.

        file_name - Name of the file to be parsed.
        """
        temp_data = {}
        #initialize csv file for reading.
        csv_file = open(file_name)
        readCSV = csv.reader(csv_file, delimiter=',')

        #Iterate through the data set starting at the second row.
        row_num = 2
        next(readCSV)
        for row in readCSV:
            #Create a new shell to fill.
            new_shell = dict(shell)
            #Fill the new shell.
            for col, key in zip(row, shell.keys()):
                new_shell[key] = col
            #Add new entry to the overall data_set
            temp_data[row_num] = new_shell
            row_num += 1
        csv_file.close()
        return temp_data
        