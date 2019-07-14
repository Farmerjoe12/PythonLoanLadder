from Loan import Loan
import matplotlib.pyplot as plt

class AmortizationView:


    def plot_single_amortization(self, loan):
        """ View the amortization chart of a single loan.

            Args:
            loan: The loan to view
        """
        amort_list = loan.get_amortization(loan.principal)

        plt.title(loan.name)
        self._plot_loan(amort_list)
        plt.show()

    
    def plot_list_amortization(self, loan_list):
        """ View the amortization chart of a list of loans.

            Args:
            loan_list: The list of loans to view
        """
        amort_list = []

        for loan in loan_list:
            amort_list.append(loan.get_amortization_list(loan.principal))

        plt.title("Amortization of multiple loans")
        self._plot_all_loans(amort_list)
        plt.show()


    def plot_comparison(self, amort_list1, amort_list2, term, principal):
        plt.title("Loan comparison")

        self._plot_loan(amort_list1)
        self._plot_loan(amort_list2)
            
        self._format_plot(term+10, principal+1000)

        plt.show()


    def _format_plot(self, term_length, max_principal):
        plt.axis([0,term_length, 0,max_principal])
        plt.grid(b=True, which='both', axis='both')
        plt.xlabel("Months")
        plt.ylabel("Dollars")


    def _plot(self, interest, principal, balance, term):
        int_line, = plt.plot(term, interest, 'b', linewidth=1.0)
        int_line.set_label('Total Interest Paid')
        plt.legend()

        princ_line, = plt.plot(term, principal, 'g', linewidth=1.0)
        princ_line.set_label('Total Principal Paid')
        plt.legend()

        bal_line, = plt.plot(term, balance, 'r', linewidth=1.0)
        bal_line.set_label('Total Balance')
        plt.legend()

    
    def _plot_loan(self, amort_list):
        """ Convert an amortization list into a plottable format. An amortization
            consists of a variety of data points, over time the data compounds
            to show a trend which can be visualized in a graph.

            Args:
            amort_list: An amortization
        """
        total_interest_paid = []
        total_principal_paid = []
        balance_remaining = []
        term = []

        total_interest = 0
        total_principal = 0
        for i in range (len(amort_list)):
            total_interest += amort_list[i][0]
            total_interest_paid.append(total_interest)

            total_principal += amort_list[i][1]
            total_principal_paid.append(total_principal)

            balance_remaining.append(amort_list[i][2])

            term.append(i)
        
        self._plot(total_interest_paid, total_principal_paid, balance_remaining, term)


    def _plot_all_loans(self, amort_list):
        total_interest_paid = []
        total_principal_paid = []
        balance_remaining = []
        term = []

        total_interest = 0
        total_principal = 0

        for i in range(len(amort_list[0])):
            term.append(i)
            total_balance = 0

            for amort in amort_list:
                total_interest += amort[i][0]
                total_principal += amort[i][1]
                total_balance += amort[i][2]

            total_interest_paid.append(total_interest)
            total_principal_paid.append(total_principal)
            balance_remaining.append(total_balance)
    
        self._plot(total_interest_paid, total_principal_paid, balance_remaining, term)


if __name__ == "__main__":
    loan_0666 = Loan("Loan 0666", 6.66, 15000, 15)
    loan_06662 = Loan("Loan 06662", 6.66, 15000, 10)

    view = AmortizationView()
    view.plot_single_amortization(loan_0666)