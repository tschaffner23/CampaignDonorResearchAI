#Donor AI

#Python imports.
#Part of the Python base modules.
import csv, os, pprint

#Non-base modules
import Parsing as pa

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
    new_parser = pa.DataParser()
    #Empty dict that will contain subdicts representing each row.
    data_set = new_parser.parse_csv('volunteer_sample_2.csv')
    pp.pprint(data_set)

if __name__ == '__main__':
    main()