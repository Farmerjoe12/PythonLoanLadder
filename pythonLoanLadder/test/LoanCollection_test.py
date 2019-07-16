import unittest

from model.Loan import Loan
from model.LoanCollection import LoanCollection


class LoanCollection_test(unittest.TestCase):
    
    
    def setUp(self):
        self.l1 = Loan("Loan 1", 2.45, 15000)
        self.l2 = Loan("Loan 2", 3.24, 15000)
        self.l3 = Loan("Loan 3", 1.34, 15000)
        self.l4 = Loan("Loan 4", 0.24, 15000)
        
        self.loans = [self.l1, self.l2, self.l3, self.l4]
        self.target = LoanCollection(self.loans)
        
        
    def test_to_string(self):
        fixtureString = "4 loans in collection\n"
        fixtureString += "========\n"
        fixtureString += self.l1.to_string() + "\n"
        fixtureString += "========\n"
        fixtureString += self.l2.to_string() + "\n"
        fixtureString += "========\n"
        fixtureString += self.l3.to_string() + "\n"
        fixtureString += "========\n"
        fixtureString += self.l4.to_string() + "\n"
        fixtureString += "========\n"
        
        self.assertEquals(fixtureString, self.target.to_string())
        
    
    def test_sort_by_interest_aesc(self):        
        loans = self.target.sort_by_interest_rate()
        
        self.assertEquals(self.l4, loans[0])
        self.assertEquals(self.l3, loans[1])
        self.assertEquals(self.l1, loans[2])
        self.assertEquals(self.l2, loans[3])
        
    
    def test_sort_by_interest_desc(self):        
        self.target.sort_by_interest_rate("desc")
        
        self.assertEqual(self.l2, self.loans[0])
        self.assertEqual(self.l1, self.loans[1])
        self.assertEqual(self.l3, self.loans[2])
        self.assertEqual(self.l4, self.loans[3])
        
        
    def test_sort_by_principal_aesc(self):
        l1 = Loan("Loan 1", 2.45, 12000)
        l2 = Loan("Loan 2", 3.24, 1000)
        l3 = Loan("Loan 3", 1.34, 5000)
        l4 = Loan("Loan 4", 0.24, 15000)
        
        loans = [l1, l2, l3, l4]
        target = LoanCollection(loans)
        target.sort_by_principal()
        
        self.assertEqual(l2, loans[0])
        self.assertEqual(l3, loans[1])
        self.assertEqual(l1, loans[2])
        self.assertEqual(l4, loans[3])
        
        
    def test_sort_by_principal_desc(self):
        l1 = Loan("Loan 1", 2.45, 12000)
        l2 = Loan("Loan 2", 3.24, 1000)
        l3 = Loan("Loan 3", 1.34, 5000)
        l4 = Loan("Loan 4", 0.24, 15000)
        
        loans = [l1, l2, l3, l4]
        target = LoanCollection(loans)
        target.sort_by_principal("desc")
        
        self.assertEqual(l4, loans[0])
        self.assertEqual(l1, loans[1])
        self.assertEqual(l3, loans[2])
        self.assertEqual(l2, loans[3])
        

    def test_get_loan_by_name_exists(self):
        loan = self.target.get_loan_by_name("Loan 1")

        self.assertIsNotNone(loan)
        self.assertEqual(2.45, loan.get_interest_rate())
        self.assertEqual(15000, loan.get_principal())

        loan = self.target.get_loan_by_name("Loan 4")

        self.assertIsNotNone(loan)
        self.assertEqual(0.24, loan.get_interest_rate())
        self.assertEqual(15000, loan.get_principal())

    
    def test_get_loan_by_name_does_not_exist(self):
        loan = self.target.get_loan_by_name("Null Loan")

        self.assertIsNone(loan)

        loan = self.target.get_loan_by_name("")

        self.assertIsNone(loan)


    def test_get_loan_by_idx_exists(self):
        loan = self.target.get_loan_by_index(0)

        self.assertIsNotNone(loan)
        self.assertEqual(2.45, loan.get_interest_rate())
        self.assertEqual(15000, loan.get_principal())

        loan = self.target.get_loan_by_index(3)

        self.assertIsNotNone(loan)
        self.assertEqual(0.24, loan.get_interest_rate())
        self.assertEqual(15000, loan.get_principal())

    
    def test_get_loan_by_idx_does_not_exist(self):
        loan = self.target.get_loan_by_index(10)

        self.assertIsNone(loan)

        loan = self.target.get_loan_by_index(-1)

        self.assertIsNone(loan)


if __name__ == '__main__':
    unittest.main()