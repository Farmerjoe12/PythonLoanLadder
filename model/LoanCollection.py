from . import Loan

class LoanCollection:
    """ A list of loans.
    
        Args:
        loan_list: Loans in a collection to operate on
    """
    def __init__(self, loan_list):
        self._loan_list = loan_list
        
        
    def to_string(self):
        print("{} loans in collection".format(len(self._loan_list)))
        print("========")
        for loan in self._loan_list:
            print(loan.to_string())
            print("========")

            
    def sort_by_interest_rate(self, order=aesc):
        if order==desc:
            sorted(self._loan_list, key=_get_interest_rate_key, reverse=True)
        elif order==aesc:
            sorted(self._loan_list, key=_get_interest_rate_key)
        else:
            pass    
    
    
    def sort_by_principal(self, order=aesc):
        if order==desc:
            sorted(self._loan_list, key=_get_principal_key, reverse=True)
        elif order==aesc:
            sorted(self._loan_list, key=_get_principal_key)
        else:
            pass    


    def _get_interest_rate_key(self, loan):
        return loan.get_interest_rate()
    
    
    def _get_principal_key(self, loan):
        return loan.get_principal()
