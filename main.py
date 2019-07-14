from model.LoanExcelDAO import LoanExcelDAO
from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule
from view.AmortizationView import AmortizationView


def _print_int_rates(loan_list):
    counter = 0
    for loan in loan_list:
        print("Loan #{} - {}".format(counter, loan.interest_rate))
        counter+=1


path = "C:\\Users\\Adam\\OneDrive - Arizona State University\\~School\\Finances.xlsx"
target = Loan("Loan 0666", interest_rate=6.66, principal=15000)
target2 = Loan("Loan 0555", interest_rate=6.66, principal=15000)

amort = RepaymentSchedule(target, 15)
schedule = amort.get_payment_schedule()

view = AmortizationView()
view.plot_single_payment_sched(schedule, target.get_name())