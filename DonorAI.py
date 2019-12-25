#Donor AI

#Python imports.
#Part of the Python base modules.
import csv, os, pprint

#Non-base modules
import Parsing as pa

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
    pp.pprint(data_set)

if __name__ == '__main__':
    main()