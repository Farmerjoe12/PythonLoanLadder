import unittest
from.context import model as model
from model.LoanExcelDAO import LoanExcelDAO

class LoanExcelDAO_test(unittest.TestCase):


    def test_loan_list_size(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        loans = target.get_loans()
        self.assertEqual(len(loans), 8)
        
if __name__ == "__main__":
    unittest.main()