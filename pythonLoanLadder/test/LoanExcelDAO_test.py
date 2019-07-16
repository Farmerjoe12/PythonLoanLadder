import unittest
from pathlib import Path
from model.LoanExcelDAO import LoanExcelDAO

path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"

@unittest.skipUnless(Path(path).is_file() == True, "Test file doesn't exist")
class LoanExcelDAO_test(unittest.TestCase):


    def test_loan_list_size(self):
        target = LoanExcelDAO(path)
        loans = target.get_loans()
        self.assertEqual(len(loans), 8)


if __name__ == '__main__':
    unittest.main()