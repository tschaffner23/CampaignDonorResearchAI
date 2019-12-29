#Donor AI

#Python imports.
#Part of the Python base modules.
import csv, os, pprint

#Non-base modules
import Parsing as pa
from webbot import Browser
import Communications

#data variables initialized for later use.

#Hard codde urls to contact.
login_addr = 'https://www.texasvan.com/Login.aspx?mode=done&authType=4'
search_addr = 'https://www.texasvan.com/QuickLookUp.aspx'
#Redircts you to the lgoin page, gives you a new cookie as well!.
redir_func = 'https://www.texasvan.com/OpenIdConnectLoginInitiator.ashx?ProviderID=4'

def main():
    #pprinter for debugging and visdualizing data usage.
    pp = pprint.PrettyPrinter(indent=2)

    #List all files in the cwd.
    os.listdir('.')
    new_parser = pa.DataParser()
    #Empty dict that will contain subdicts representing each row.
    data_set = new_parser.parse_csv('volunteer_sample_2.csv')
    comm = Browser(showWindow=False)
    mappings = {
            'FirstName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterFirstName',
            'LastName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterLastName',
            'City': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterCity_DropDownListCity',
            'Cell': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterPhone',
            'Home': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterPhone',
            'Work': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterPhone',
            'StreetAddress': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'StreetAddress_2': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'Zip': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterZip',
            'Email': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterEmail_FilterEmail'
    }
    web_comm = Communications.WebComm(mappings)
    web_comm.login_van(comm, 'Slark1101', 'tschaffner23@gmail.com')
    results = []
    for key in data_set:
        result = web_comm.simple_search(comm, 'https://www.texasvan.com/QuickLookUp.aspx', ['StreetAddress', 'StreetAddress_2','City', 'Cell', 'Home', 'Work', 'Zip'], data_set[key])
        results.append((key, result))
        print(str(key) + ' done')
    pp.pprint(results)
    #pp.pprint(data_set)


if __name__ == '__main__':
    main()