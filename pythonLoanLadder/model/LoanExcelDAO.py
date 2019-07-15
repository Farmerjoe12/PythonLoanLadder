import xlrd
import re
from .Loan import Loan
from .RepaymentSchedule import RepaymentSchedule

class LoanExcelDAO:
    """ A Data Access Object which gets Loan information
        from persistant storage in the form of an Excel spreadsheet.

        Args:
        path: The absolute path to the spreadsheet on your system
    """
    def __init__(self, path):
        self._path = path
        self._loans = self._get_loan_list()


    def _get_loan_list(self):
        """ Open a workbook, parse data, and extract loan info """
        book = xlrd.open_workbook(self._path)
        loan_sheet = book.sheet_by_index(0)
        name_col = 0
        principal_col = 1
        interest_rate_col = 2

        name_reg = re.compile("^Loan [0-9]*$")
        result = []
        for row in range(loan_sheet.nrows):
            name = loan_sheet.cell(row, name_col).value
            princ = loan_sheet.cell(row, principal_col).value
            int_rate = loan_sheet.cell(row, interest_rate_col).value
            
            if name_reg.match(name):
                temp = Loan(name, int_rate, princ)
                result.append(temp)
        
        return result


    def get_loans(self):
        return self._loans