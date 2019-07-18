import sys

from PyQt5.QtWidgets import QApplication

from model.LoanExcelDAO import LoanExcelDAO
from model.Loan import Loan
from model.LoanCollection import LoanCollection
from model.RepaymentSchedule import RepaymentSchedule
# from view.AmortizationView import plot_single_payment_sched as plot
# from view.AmortizationView import plot_two_payment_sched as plot2
from view.AmortizationView import AmortizationView
from view.Window import Window


path = "C:\\Users\\AF069488\\PythonLoanLadder\\pythonLoanLadder\\data\\loanTestBook.xls"
loan_coll = LoanExcelDAO(path).get_loan_collection()


def menu():
        menu = "***********************\n"
        menu += "Enter a number to do things\n"
        menu += "1:\tView a loans information\n"
        menu += "2:\tView the graph of a loans payment schedule\n"
        menu += "3:\tQuit\n"
        menu += "**********************\n"
        menu += "\n"
        menu += "Your choice: "
        return menu


def loan_menu():
        menu = "***********************\n"
        menu += "Select a Loan\n"
        for i in range(loan_coll.get_size_of_collection()):
                menu += "{}:\t{}\n".format(i, loan_coll.get_loan_by_index(i).get_name())
        menu += "{}:\tGo back\n".format(i+1)
        menu += "**********************\n"
        menu += "\n"
        menu += "Your choice: "
        return menu


def view_loan_info():
        while(True):
                choice = input(loan_menu())
                if int(choice) in range(loan_coll.get_size_of_collection()):
                        loan = loan_coll.get_loan_by_index(int(choice))
                        print_loan_info(loan)
                        print("\n")

                elif int(choice) == loan_coll.get_size_of_collection():
                        return

                elif int(choice) not in range(loan_coll.get_size_of_collection()):
                        print("\nChoice not valid\n")


def print_loan_info(loan):
        repayment_info = ""
        while True:
                choice = input("Would you like to see a repayment schedule (y/n): ")
                if choice == "y":
                        term = input("\nEnter term length (years): ")
                        sched = RepaymentSchedule(loan, int(term))
                        repayment_info = sched.to_string()
                        break
                elif choice == "n":
                        break
                else:
                        print("\nInvalid choice")

        loan_info = "==== {} Info ====\n".format(loan.get_name())
        loan_info += loan.to_string()
        if (repayment_info != ""):
                loan_info += "\n===== Payment Info ====\n"
                loan_info += repayment_info
        print(loan_info)


def view_loan_pymt_sched():
        while(True):
                choice = input(loan_menu())
                if int(choice) in range(loan_coll.get_size_of_collection()):
                        term = input("\nEnter term length (years): ")
                        graph_loan(loan_coll.get_loan_by_index(int(choice)), int(term))
                        print("\n")

                elif int(choice) == loan_coll.get_size_of_collection():
                        return

                elif int(choice) not in range(loan_coll.get_size_of_collection()):
                        print("\nChoice not valid\n")


def graph_loan(loan, term):
        sched = RepaymentSchedule(loan, term).get_payment_schedule()
        view = plot(sched, loan.get_name())


""" Main application """
def main():
    """ Comparing two repayment terms against the same loan
    loan1 = Loan("Loan 1", 2.45, 15000)
    sched1 = RepaymentSchedule(loan1, 15).get_payment_schedule()
    sched2 = RepaymentSchedule(loan1, 5).get_payment_schedule()

    plot2(sched1, "Loan 1 15 yr term", sched2, "Loan 1 5 yr term")
    """
    while True:
        choice = input(menu())
        if choice == "1":
                view_loan_info()

        elif choice == "2":
                view_loan_pymt_sched()

        elif choice == "3":
                print("\nGoodbye")
                quit()

        else:
                print("\nChoice not valid\n")
        


if __name__ == '__main__':
        # main()
        
        loan = Loan("Loan 666", 6.66, 15000)
        sched = RepaymentSchedule(loan, 15).get_payment_schedule()

        app = QApplication(sys.argv)

        ex = Window()
        view = AmortizationView(parent=ex, payment_schedule=sched)
        ex.show()
        
        sys.exit(app.exec_())
