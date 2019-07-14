from Loan import Loan
import math

class RepaymentSchedule:
    """ A wrapper class for a Loan which is used to calculate the 
        repayment schedule for a given Loan over a given Term.

        Args:
        loan: The loan which is being repaid
        term: The term for which the repayment schedule is calculated
    """
    def __init__(self, loan, term):
        self._loan = loan
        self._term = term
        self._monthly_payment = self._get_monthly_payment()


    def get_payment_schedule(self, additional=0):
        """ Get the payment schedule.
    
            A payment schedule (aka amortization schedule) is a schedule
            of payments over time. Each payment will have component parts
            which are split between paying interest and 
            the principal balance of the loan
        """
        total_princ = self._loan.principal
        amort_list = []

        while total_princ > 0:
            amort = self._get_installment(total_princ, additional)
            total_princ -= amort[1] # amort[1] is the quant paid to principal
            amort_list.append(amort)

        return amort_list


    def _get_installment(self, princ, additional):
        """ Get an installment payment for a specific amount of principal.
        
            Using a principal, return a tri-tuple of quantities
            representing the component parts of a monthly installment (payment)
            which are paid to interest and principal. The third component of 
            the tuple is the remaining balance after the payment is applied.

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
        monthly_rate = self._loan.interest_rate/12
        monthly_interest = monthly_rate * princ

        principal_repayment = self._monthly_payment - monthly_interest
        principal_repayment += additional

        principal_remaining = princ - principal_repayment

        return monthly_interest, principal_repayment, principal_remaining


    def _get_monthly_payment(self):
        """ Calculate the monthly payment.

            Formula comes from:
            https://www.wikihow.com/Calculate-Loan-Payments

        """
        interest_rate = self._loan.interest_rate

        if interest_rate > 0:
            eff_int_rate = interest_rate / 12
            total_payments = self._term * 12

            step_1 = (1+eff_int_rate)**(-total_payments)
            step_2 = eff_int_rate / (1-step_1)
            monthly_payment = self._loan.principal * step_2
        else:
            monthly_payment = self._loan.principal/(self._term*12)

        return self._round_up(monthly_payment, 2)
        

    def _round_up(self, n, decimals=0):
        multiplier = 10**decimals
        return math.ceil(n*multiplier) / multiplier

    
    def get_term(self):
        return self._term

    
    def get_loan(self):
        return self._loan

    def get_monthly_payment(self):
        return self._monthly_payment