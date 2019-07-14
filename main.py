from LoanExcelDAO import LoanExcelDAO
from Loan import Loan
from AmortizationView import AmortizationView


def _print_int_rates(loan_list):
    counter = 0
    for loan in loan_list:
        print("Loan #{} - {}".format(counter, loan.interest_rate))
        counter+=1


path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
target = Loan("Loan 0666", interest_rate=6.66, principal=15000, term=15)
target2 = Loan("Loan 0555", interest_rate=6.66, principal=15000, term=5)

amort_list = target.get_amortization(target.principal)
amort_list2 = target2.get_amortization(target2.principal)

view = AmortizationView()
view.plot_single_amortization(target)
view.plot_single_amortization(target2)
view.plot_comparison(amort_list, amort_list2, target.term*12, target.principal)