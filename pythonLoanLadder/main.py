from model.LoanExcelDAO import LoanExcelDAO
from model.Loan import Loan
from model.LoanCollection import LoanCollection
from model.RepaymentSchedule import RepaymentSchedule
from view.AmortizationView import AmortizationView


path = "C:\\Users\\AF069488\\PythonLoanLadder\\pythonLoanLadder\\data\\loanTestBook.xls"
loan_coll = LoanExcelDAO(path).get_loan_collection()


def menu():
        menu = "***********************\n"
        menu += "Enter a number to do things\n"
        menu += "1:\tView a loan\n"
        menu += "2:\tQuit\n"
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


def get_loan_choice():
        while(True):
                choice = input(loan_menu())
                if int(choice) in range(loan_coll.get_size_of_collection()):
                        print(loan_coll.get_loan_by_index(int(choice)).to_string())
                        print("\n")

                elif int(choice) == loan_coll.get_size_of_collection():
                        return

                elif int(choice) not in range(loan_coll.get_size_of_collection()):
                        print("\nChoice not valid\n")


def main():
        while(True):
                choice = input(menu())
                if choice == "1":
                        get_loan_choice()

                elif choice == "2":
                        print("\nGoodbye")
                        quit()
                        
                else:
                        print("\nChoice not valid\n")


if __name__ == '__main__':
        main()