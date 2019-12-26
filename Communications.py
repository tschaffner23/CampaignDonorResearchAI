#Web communications class(es)

#Python base module imports.
from webbot import Browser
from Verification import Verify

class WebComm():

    """
    Class used to coomunicate with websites.
    """

    def __init__(self, id_mappings):
        """
        Constructor for the WebComm class.

        id_mapping - dictionary containing mappings of data_set keys
        to ids of filter boxes for a given website.
        """
        self.id_mappings = id_mappings
        #Pass an empty list of terms for now.
        self.verifier = Verify([])
    
    def login_van(self, comm, password, username):
        
        """
        Login using the given url and credentials.

        url - url address of lgin website.
        password - password used to login.
        username - username used to login.
        """
        comm.go_to('https://www.texasvan.com/OpenIdConnectLoginInitiator.ashx?ProviderID=4')
        #comm.click('Log in with ActionID')
        comm.type(username, into='username')
        comm.type(password, into='password')
        comm.click('Log in')
    
    def simple_search(self, comm, url, terms, dataset):
        
        """
        Search for a person using only their first and last names
        and one other piece of info.

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
        confirmed_full_name = ''
        #Search the VAN databse using the first/last name of a person
        #and one other criteria.
        for term in terms:
            comm.type(last, id=self.id_mappings['LastName'])
            comm.type(first, id=self.id_mappings['FirstName'])
            comm.type(dataset[term], id=self.id_mappings[term])
            comm.click('Search')
            #Get search results in a list.
            results = [e.text for e in comm.find_elements(tag='td')]
            #Check if the target person is in the results.
            confimed_data = self.verifier.verify_person(dataset, results, 6)
            if confimed_data is not None:
                confirmed_full_name = confimed_data[0]
                break
        return confirmed_full_name






