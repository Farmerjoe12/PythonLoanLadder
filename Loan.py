import numpy
import math
import unittest

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
        self.name = name
        if (interest_rate > 1):
            self.interest_rate = interest_rate/100
        else:
            self.interest_rate = interest_rate
        self.principal = principal


    def to_string(self):
        result = "Loan Name: {}\nPrincipal: {}\n".format(self.name, self.principal)
        result += "Interest Rate: {}".format(self.interest_rate)
        return result