# CampaignDonorReasearchAI
An AI to do campaign donor research so that I don't have to.

# Libraries used:
    -unittest, for writing unit tests for my code. Part of the base python package.
    -csv, for parsing out data from csv files. Part of the python base modules.
    -random, for generating random numbers used for testing. Part of the python base modules.

# Files:

## Testing.py:
    -Contains multiple classes that inherit from unittest.TestCase used for testing.
    -Uses unittest, csv, random, DonorAI, and Parsing modules.

## Parsing.py:
    -Contains a DataParser class that can be used to parse data from csv files and websites.
    -Uses csv module.

## Communications.py:
    -Contains a WebComm class that sends HTTP/HTTPS requests and stores cookies for login.
    -Uses http.cookiejar, urllib.request, urllib.parse modules.
