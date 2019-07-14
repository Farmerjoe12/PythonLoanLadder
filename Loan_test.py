import unittest
from Loan import Loan

class Loan_test(unittest.TestCase):
    

    def test_round_up(self):
        target = Loan("Loan 0666", 6.66, 15000, 15)
        self.assertEqual(target._round_up(n = 131.9234), 132)
        self.assertEqual(target._round_up(131.1323, 2), 131.14)


    def test_get_monthly_payment(self):
        target = Loan("Loan 0666", 6.66, 15000, 15)
        self.assertEqual(target.monthly_payment, 131.99)
        target = Loan("Loan 0666", 4.865, 22687.87, 15)
        self.assertEqual(target.monthly_payment, 177.83)
        target = Loan("Loan 0666", 6.365, 14447.63, 15)
        self.assertEqual(target.monthly_payment, 124.79)


    def test_to_string(self):
        target = Loan("Loan 0666", 6.66, 15000, 15)
        expected = "Loan Name: {}\nPrincipal: {}\n".format("Loan 0666", 15000)
        expected += "Interest Rate: {}\nTerm: {}".format(0.0666, 15)
        self.assertEqual(target.to_string(), expected)


    def test_get_installment(self):
        target = Loan("Loan 0666", 6.66, 15000, 15)
        expected_monthly_interest, expected_principal_repayment, expected_principal_remaining = target._get_installment(target.principal, 0)
        
        self.assertAlmostEqual(expected_monthly_interest, 83.25, delta = .05)
        self.assertAlmostEqual(expected_principal_repayment, 48.74, delta = .05)
        self.assertAlmostEqual(expected_principal_remaining, 14951.26, delta = .05)


    def test_get_installment_with_additional(self):
        target = Loan("Loan 0666", 6.66, 15000, 15)
        expected_monthly_interest, expected_principal_repayment, expected_principal_remaining = target._get_installment(target.principal, additional=50)
        
        self.assertAlmostEqual(expected_monthly_interest, 83.25, delta = .05)
        self.assertAlmostEqual(expected_principal_repayment, 98.74, delta = .05)
        self.assertAlmostEqual(expected_principal_remaining, 14901.26, delta = .05)


    def test_get_amortization_no_interest(self):
        target_loan = Loan("", 0, 1200, 1)
        target_amort = target_loan.get_amortization(1200)
        
        for i in range(len(target_amort)):
            interest, princ_pay, princ_remain = target_amort[i]

            self.assertEqual(0, interest)
            self.assertEqual(100, princ_pay)
            self.assertEqual(1200 - 100*(i+1), princ_remain)

            
if __name__ == '__main__':
    unittest.main()