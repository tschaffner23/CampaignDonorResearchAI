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
        #Search the VAN databse using the first/last name of a person
        #and one other criteria.
        for term in terms:
            #If there is no entry for the search term ignore it.
            if dataset[term] == '':
                continue
            comm.type(dataset['LastName'], id=self.id_mappings['LastName'])
            comm.type(dataset['FirstName'], id=self.id_mappings['FirstName'])
            comm.type(dataset[term], id=self.id_mappings[term])
            comm.click('Search')
            #Get search results in a list.
            results = [e.text for e in comm.find_elements(tag='td')]
            #Check if the target person is in the results.
            confirmed_first_name = self.verifier.verify_person(dataset, results, 6)
            if confirmed_first_name is not None:
                comm.click(confirmed_first_name)
                return comm.get_current_url()
            #Clear search filters and search again.
            comm.click('Clear')
        return None

    def scrape_data(self, comm, confirmed_full_name):

        """
        Scrape user dat from the VAN website. Keeping as a method for now
        rather than a distinct class for times sake. Not particulary dynamic
        or robust.

        comm - webbot Browser object that communicates with a web page.
        confirmed_full_name - full name of a confirmed target.
        """
        print(comm.get_current_url())
        stuff = comm.find_elements(css_selector='#ContactsDetailsPageSectionsTab > div.row-golden > div.col-wide.ui-sortable > div:nth-child(6)', loose_match=False)
        #/html/body/form/div[3]/div[3]/div/div[2]/div[2]/div/div[1]/div[2]/div[6]/div/div/div/div[2]/table/tbody/tr[2]
        #ContactsDetailsPageSectionsTab > div.row-golden > div.col-wide.ui-sortable > div:nth-child(6)
        #ContactsDetailsPageSectionsTab > div.row-golden > div.col-wide.ui-sortable > div:nth-child(6)
        #ctl00_ContentPlaceHolderVANPage_ctl32_innerContentPanel_Phones_EIDFA1F7B1F_Content > table > tbody > tr:nth-child(2)
        #ctl00_ContentPlaceHolderVANPage_ctl32_innerContentPanel_Phones_EIDFA1F7B1F_Content > table > tbody
        print(stuff)
        print('Dicks', '\n')
        for s in stuff:
            print(s.find_element_by_id('ctl00_ContentPlaceHolderVANPage_ctl32_ctl08_ctl01_EIDFA1F7B1FPhonesFullPhone'))