import numpy
import math
import unittest

class Loan:


    def __init__(self, name, interest_rate, principal, term):
        self.name = name
        if (interest_rate > 1):
            self.interest_rate = interest_rate/100
        else:
            self.interest_rate = interest_rate
        self.principal = principal
        self.term = term
        self.monthly_payment = self._get_monthly_payment()


    def get_amortization(self, princ, additional=0):
        """ Using a total principal, return a list of payments.

            Args:
            princ: The principal of a loan to repay

            Return: A list of tuples representing the amortization of a loan
        """
        amort_list = []
        if princ > 0:
            amort = self._get_installment(princ, additional)
            amort_list.append(amort)
            princ_remain = amort[2]
            amort_list += self.get_amortization(princ_remain)
        return amort_list


    def _get_installment(self, princ, additional):
        """ Using a total princpal, return a tri-tuple of payments
            representing the component parts of a payment which are paid
            to interest and principal, and the remaining balance after
            the payment is applied.

            Optionally, an additional amount can be applied directly to the
            principal after the interest is paid.

            Args:
            princ: The principal of a loan which is being paid
            additional: Any additional funding which is paid directly to principal

            Return:
            The amount of the payment paid towards interest,
            The amount of the payment paid towards principal,
            The amount of principal remaining after payment
        """
        monthly_rate = self.interest_rate/12
        monthly_interest = monthly_rate * princ

        principal_repayment = self.monthly_payment - monthly_interest
        principal_repayment += additional

        principal_remaining = princ - principal_repayment

        return monthly_interest, principal_repayment, principal_remaining


    def _get_monthly_payment(self):
        interest_rate_per_mth = self.interest_rate / 12
        total_payments = self.term * 12
        step_2 = (interest_rate_per_mth+1)**(-total_payments)
        step_3 = 1-step_2
        step_4 = self.principal*interest_rate_per_mth
        monthly_payment = step_4/step_3
        return self._round_up(monthly_payment, 2)
        

    def _round_up(self, n, decimals=0):
        multiplier = 10**decimals
        return math.ceil(n*multiplier) / multiplier


    def to_string(self):
        result = "Loan Name: {}\nPrincipal: {}\n".format(self.name, self.principal)
        result += "Interest Rate: {}\nTerm: {}".format(self.interest_rate, self.term)
        return result