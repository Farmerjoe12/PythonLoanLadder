import unittest
from RepaymentSchedule import RepaymentSchedule
from Loan import Loan

class RepaymentScedule_test(unittest.TestCase):


    def setUp(self):
        self.loan = Loan("Loan 0666", 6.66, 15000)

    def test_monthly_payment(self):
        target = RepaymentSchedule(self.loan, 15)
        self.assertEqual(target.get_monthly_payment(), 131.99)

        self.loan = Loan("Loan 0666", 4.865, 22687.87)
        target = RepaymentSchedule(self.loan, 15)
        self.assertEqual(target.get_monthly_payment(), 177.83)

        self.loan = Loan("Loan 0666", 6.365, 14447.63)
        target = RepaymentSchedule(self.loan, 15)
        self.assertEqual(target.get_monthly_payment(), 124.79)


    def test_get_pymt_sched_no_int_no_addtl(self):
        self.loan = Loan("", 0, 1200)
        target = RepaymentSchedule(self.loan, 1)
        target_amort = target.get_payment_schedule()
        
        for i in range(len(target_amort)):
            interest, princ_pay, princ_remain = target_amort[i]

            self.assertEqual(0, interest)
            self.assertEqual(100, princ_pay)
            self.assertEqual(1200 - 100*(i+1), princ_remain)


if __name__ == '__main__':
    unittest.main()