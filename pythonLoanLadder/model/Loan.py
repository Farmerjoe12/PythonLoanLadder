import numpy
import math

class Loan:
    """ A representation of a Loan from a financial institution.

        Loans are comprised of three main parts, a principal 
        or the amount for which the loan is disbursed, an interest rate
        because lending companies are crooked organizations which charge
        you money for borrowing their money, and a term for which 
        the repayment period is defined. 

        Fields:
        name: A descriptive name for a loan
        interest_rate: The interest rate given by a lender (%5.34)
        principal: The amount of money that is lent
        term: the repayment period (in years)
    """

    def __init__(self, name, interest_rate, principal):
        self._name = name
        self._interest_rate = interest_rate
        self._principal = principal


    def get_interest_rate(self):
        return self._interest_rate

    
    def get_principal(self):
        return self._principal


    def get_name(self):
        return self._name


    def to_string(self):
        result = "Loan Name: {}\n".format(self._name)
        result += "Principal: {}\n".format(self._principal)
        result += "Interest Rate: %{}".format(self._interest_rate)
        return result