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
        self.target.sort_by_interest()
        
        self.assertEqual(self.l4, self.target[0])
        self.assertEqual(self.l3, self.target[1])
        self.assertEqual(self.l1, self.target[2])
        self.assertEqual(self.l2, self.target[3])
        
    
    def test_sort_by_interest_desc(self):        
        self.target.sort_by_interest("desc")
        
        self.assertEqual(self.l2, self.target[0])
        self.assertEqual(self.l1, self.target[1])
        self.assertEqual(self.l3, self.target[2])
        self.assertEqual(self.l4, self.target[3])
        
        
    def test_sort_by_principal_aesc(self):
        l1 = Loan("Loan 1", 2.45, 12000)
        l2 = Loan("Loan 2", 3.24, 1000)
        l3 = Loan("Loan 3", 1.34, 5000)
        l4 = Loan("Loan 4", 0.24, 15000)
        
        loans = [l1, l2, l3, l4]
        target = LoanCollection(loans)
        target.sort_by_principal()
        
        self.assertEqual(l2, target[0])
        self.assertEqual(l3, target[1])
        self.assertEqual(l1, target[2])
        self.assertEqual(l4, target[3])
        
        
    def test_sort_by_principal_desc(self):
        l1 = Loan("Loan 1", 2.45, 12000)
        l2 = Loan("Loan 2", 3.24, 1000)
        l3 = Loan("Loan 3", 1.34, 5000)
        l4 = Loan("Loan 4", 0.24, 15000)
        
        loans = [l1, l2, l3, l4]
        target = LoanCollection(loans)
        target.sort_by_principal("desc")
        
        self.assertEqual(l4, target[0])
        self.assertEqual(l1, target[1])
        self.assertEqual(l3, target[2])
        self.assertEqual(l2, target[3])
        
    
if __name__ == '__main__':
    unittest.main()