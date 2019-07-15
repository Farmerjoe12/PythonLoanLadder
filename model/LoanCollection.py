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
