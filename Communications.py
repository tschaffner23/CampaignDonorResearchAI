#Web communications classe(s)

#Python base module imports.
import webbot

class WebComm():

    """
    Class used to coomunicate with websites.
    """

    def __init__(self):
        
        """
        Initialize class attributes.
        """
        self.comm = webbot.Browser()
    
    def login(self, url, password, username):
        
        """
        Login using the given url and credentials.

        url - url address of lgin website.
        password - password used to login.
        username - username used to login.
        """
        self.comm.go_to(url)
        self.comm.click('Log in with ActionID')
        self.comm.type(username, into='username')
        self.comm.type(password, into='password')
        self.comm.click('Log in')




