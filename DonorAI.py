#Donor AI

#Python imports.
#Part of the Python base package.
import csv
import os
import pprint

#data variables initialized for later use.

#Hard coded shell dictionary.
shell = {   'VANID': '',
            'priority': '', 
            'first': '', 
            'mid': '',
            'last': '', 
            'suf': '', 
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'zip_postal': '',
            'zip4': '',
            'country_code': '',
            'home': '',
            'cell': '',
            'work': '',
            'email': '',
            'notes': '',
            'occupation': '',
            'employer': ''
            }

def main():
    #pprinter for debugging and visdualizing data usage.
    pp = pprint.PrettyPrinter(indent=2)

    #List all files in the cwd.
    os.listdir('.')
    #Empty dict that will contain subdicts representing each row.
    data_set = parse_csv('volunteer_sample_2.csv')
    pp.pprint(data_set)

#Method for parsing our csv files given a file name.
def parse_csv(file_name):

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
        temp_data[row_num] = new_shell
        row_num += 1
    csv_file.close()
    return temp_data

if __name__ == '__main__':
    main()