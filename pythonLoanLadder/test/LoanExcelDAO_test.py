import unittest
from pathlib import Path
from model.LoanExcelDAO import LoanExcelDAO
from model.LoanCollection import LoanCollection

path = "C:\\Users\\AF069488\\PythonLoanLadder\\pythonLoanLadder\\data\\loanTestBook.xls"

@unittest.skipUnless(Path(path).is_file() == True, "Test file doesn't exist")
class LoanExcelDAO_test(unittest.TestCase):
    """ When given an Excel workbook, LoanExcelDAO will extract loan information
        from it. 
        
        The proper formatting of the columns of the workbook is:
        COL 1: Loan Name    COL 2: Principal    COL 3: Interest Rate
    """

    def setUp(self):
        self.target = LoanExcelDAO(path)
        self.loan_collection = self.target.get_loan_collection()


    def test_all_loans_are_retrieved(self):
        self.assertEqual(4, self.loan_collection.get_size_of_collection())

    def test_loan_list_type(self):
        self.assertTrue(isinstance(self.loan_collection, LoanCollection))


if __name__ == '__main__':
    unittest.main()