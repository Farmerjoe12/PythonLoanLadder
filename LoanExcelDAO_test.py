import unittest
from LoanExcelDAO import LoanExcelDAO

class LoanExcelDAO_test(unittest.TestCase):


    def test_loan_list_size(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        loans = target.loans
        self.assertEqual(len(loans), 8)


    def test_get_total_mthly_payment(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        self.assertAlmostEqual(target.get_total_mthly_payment(), 460.84, delta=.50)


    def test_sort_by_interest_rate_asc(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        loan_list = target.sort_by_interest_rate()
        fixture = [0.0429, 0.0429, 0.0466, 0.0466, 0.04865, 0.0505, 0.0505, 0.06365]
        for i in range(len(fixture)):
            self.assertEqual(loan_list[i].interest_rate, fixture[i])


    def test_sort_by_interest_rate_desc(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        loan_list = target.sort_by_interest_rate(order="desc")
        fixture = [0.0429, 0.0429, 0.0466, 0.0466, 0.04865, 0.0505, 0.0505, 0.06365]
        fixture.sort(reverse = True)
        for i in range(len(fixture)):
            self.assertEqual(loan_list[i].interest_rate, fixture[i])


    def test_get_total_principal(self):
        path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
        target = LoanExcelDAO(path)
        self.assertAlmostEqual(target.get_total_principal(), 57565.23, delta=0.5)

        
if __name__ == "__main__":
    unittest.main()