from . import Loan


class LoanCollection:
    """ A list of loans.
    
        Args:
        loan_list: Loans in a collection to operate on
    """

    def __init__(self, loan_list):
        self._loan_list = loan_list

    def to_string(self):
        """ Convert this list of loans into a descriptive string """
        result = "{} loans in collection\n".format(len(self._loan_list))
        result += ("========\n")
        for loan in self._loan_list:
            result += (loan.to_string() + "\n")
            result += ("========\n")
        return result

    def to_html(self):
        result = "<h2>Loan Collection</h2>" + "\n"
        result += "<h3>=========</h3>" + "\n"
        for loan in self._loan_list:
            result += loan.to_html()
            result +="<h3>=========</h3>" + "\n"
        return result

    def sort_by_interest_rate(self, order="aesc"):
        """ Sort the collection of loans by interest rate
        
            Args:
            order: Either 'aesc' or 'desc' for aescending or descending
        """
        if order == "desc":
            self._loan_list.sort(key=self._get_interest_rate_key, reverse=True)
            return self._loan_list
        elif order == "aesc":
            self._loan_list.sort(key=lambda loan: loan.get_interest_rate())
            return self._loan_list
        else:
            pass

    def sort_by_principal(self, order="aesc"):
        """ Sort the collection of loans by principal amount
        
            Args:
            order: Either 'aesc' or 'desc' for aescending or descending
        """
        if order == "desc":
            return self._loan_list.sort(key=lambda loan: loan.get_principal(), reverse=True)
        elif order == "aesc":
            return self._loan_list.sort(key=lambda loan: loan.get_principal())
        else:
            pass

    def get_loan_by_index(self, idx):
        """ Get a loan from the collection.

            Args:
            idx: The position of the loan to get

            Return:
            The loan or None
        """
        if idx not in range(self.get_size_of_collection()):
            return None
        else:
            return self._loan_list[idx]

    def get_loan_by_name(self, name):
        """ Get a loan from the collection.

            Args:
            name: The name of the loan to find

            Return:
            The loan or None
        """
        if name == "":
            return None

        for loan in self._loan_list:
            if loan.get_name() == name:
                return loan

        return None

    def _get_interest_rate_key(self, loan):
        return loan.get_interest_rate()

    def _get_principal_key(self, loan):
        return loan.get_principal()

    def get_size_of_collection(self):
        return len(self._loan_list)
