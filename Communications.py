#Web communications classe(s)

#Python base module imports.
from webbot import Browser

class WebComm():

    """
    Class used to coomunicate with websites.
    """

    def __init__(self):
        """
        Constructor for the WebComm class.

        id_mapping - dictionary containing mappings of data_set keys
        to ids of filter boxes on the VAN search page.
        """
        self.id_mapping = {
            'FirstName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterFirstName',
            'LastName': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterLastName',
            'City': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterCity_DropDownListCity',
            'Phone': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterPhone',
            'StreetAddress': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'StreetAddress_2': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterStreetAddress',
            'Zip': 'ctl00_ContentPlaceHolderVANPage_ctl00_TextBoxFilterZip',
            'Email': 'ctl00_ContentPlaceHolderVANPage_ctl00_VANInputItemFilterEmail_FilterEmail'
        }
    
    def login(self, comm, url, password, username):
        
        """
        Login using the given url and credentials.

        url - url address of lgin website.
        password - password used to login.
        username - username used to login.
        """
        comm.go_to(url)
        comm.click('Log in with ActionID')
        comm.type(username, into='username')
        comm.type(password, into='password')
        comm.click('Log in')
    
    def search(self, comm, url, terms, dataset):
        
        """
        Search for a person in the search bar.

        comm - webbot Browser object that communicates with a web page.
        url - url to connect to.
        terms - list of terms relating to filtering a search. Used as both 
        keys into the dataset and identifiers for finding the filter boxes
        on the VAN search webpage.
        dataset - dictionary containing info on a specific voter.
        """
        comm.go_to(url)
        first = dataset['FirstName']
        last = dataset['LastName']
        for term in terms:
            comm.type(last, id=self.id_mapping['LastName'])
            comm.type(first, id=self.id_mapping['FirstName'])
            comm.type(dataset[term], id=self.id_mapping[term])
            comm.click('Search')





