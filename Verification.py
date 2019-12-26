#Data verification class(es)

class Verify():

    """
    Class used to verify if a person has been found.
    """

    def __init__(self, terms):
        
        """
        Constructor class for Verify.

        terms - list of terms to use for verifying search results.
        """
        self.search_confirmation_terms = terms


    def verify_person(self, dataset, results, step):
        
        """
        Verify that the person being searched for is in the
        search results. Return a list slice if the person is there,
        otherwise return empty list.

        dataset - Dictionary of info on the person being searched for.
        results - List containing the results of the search.
        step - step size used to splice out data from search results.

        """
        #Splice out each persons individual data.
        front = 0
        spliced_results = []
        for x in range(6, len(results), step):
            spliced_results.append(results[front:x])
            front += step
        #Verify address:
        for splice in spliced_results:
            addr = splice[1].strip()
            if addr == dataset['StreetAddress'].strip() or addr == dataset["StreetAddress_2"].strip():
                return splice
        return None
        




        