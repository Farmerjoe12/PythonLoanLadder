import xlrd
import re
from Loan import Loan

class LoanExcelDAO:
    
    def __init__(self, path, term=15):
        self.path = path
        self.loans = self._get_loan_list(term)


    def sort_by_interest_rate(self, order="asc"):
        if order == "desc":
            result = sorted(self.loans, key=lambda loan:loan.interest_rate, reverse=True)
        else:
            result = sorted(self.loans, key=lambda loan: loan.interest_rate)
        return result


    def get_total_mthly_payment(self):
        result = 0
        for loan in self.loans:
            pmt = loan.monthly_payment
            result += pmt

        return result


    def get_total_principal(self):
        result = 0
        for loan in self.loans:
            result += loan.principal
        return result


    def _get_loan_list(self, term):
        book = xlrd.open_workbook(self.path)
        loan_sheet = book.sheet_by_index(0)
        name_col = 0
        principal_col = 1
        interest_rate_col = 2
        term_col = 3

        name_reg = re.compile("^Loan [0-9]*$")
        loans = []
        for row in range(loan_sheet.nrows):
            name = loan_sheet.cell(row, name_col).value
            princ = loan_sheet.cell(row, principal_col).value
            int_rate = loan_sheet.cell(row, interest_rate_col).value
            term_val = loan_sheet.cell(row, term_col).value
            
            if name_reg.match(name):
                if int(term_val) > term:
                    term_val = term
                temp = Loan(name, int_rate, princ, term_val)
                loans.append(temp)
        
        return loans