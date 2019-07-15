import unittest
from.context import model as model
from model.LoanCollection import LoanCollection

class LoanCollection_test(unittest.TestCase):
    
    
    def setup(self):
        l1 = Loan("Loan 1", 2.45, 15000)
        l2 = Loan("Loan 2", 3.24, 15000)
        l3 = Loan("Loan 3", 1.34, 15000)
        l4 = Loan("Loan 4", 0.24, 15000)
        
        loans = [l1, l2, l3, l4]
        target = LoanCollection(loans)
        
    
    def test_sort_by_interest_aesc(self):        
        target.sort_by_interest()
        
        self.assertEqual(l4, target[0])
        self.assertEqual(l3, target[1])
        self.assertEqual(l1, target[2])
        self.assertEqual(l2, target[3])
        
    
    def test_sort_by_interest_desc(self):        
        target.sort_by_interest(desc)
        
        self.assertEqual(l2, target[0])
        self.assertEqual(l1, target[1])
        self.assertEqual(l3, target[2])
        self.assertEqual(l4, target[3])
        
        
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
        target.sort_by_principal()
        
        self.assertEqual(l4, target[0])
        self.assertEqual(l1, target[1])
        self.assertEqual(l3, target[2])
        self.assertEqual(l2, target[3])
        
    
if "__name__" == "__main__":
    unittest.main()
