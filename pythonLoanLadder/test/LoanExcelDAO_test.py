import unittest
from pathlib import Path
from model.LoanExcelDAO import LoanExcelDAO

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
        self.loans = self.target.get_loans()


    def test_loan_list_size(self):
        self.assertEqual(len(self.loans), 4)


    def test_loan_list_contents(self):
        self.assertEqual(15000, self.loans[0].get_principal())
        self.assertEqual(0, self.loans[0].get_interest_rate())

        self.assertEqual(23495.23, self.loans[3].get_principal())
        self.assertEqual(6.5, self.loans[3].get_interest_rate())


if __name__ == '__main__':
    unittest.main()