from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule
import matplotlib.pyplot as plt

""" A Repayment Schedule can be viewed convieniently in a graph format.

    The graph shows the amounts paid to interest and principal over time,
    as well as the principal remaining throughout the term.
"""
    
def plot_single_payment_sched(schedule, title):
    """ View the payment schedule of a single loan in graph format.

        Args:
        schedule: The payment schedule of a loan
    """
    plt.title(title)
    _plot_loan(schedule)
    plt.grid(True)
    plt.show()


def plot_two_payment_sched(sched1, title1, sched2, title2):
    """ Plot two payment schedules side by side:

        Args:
        sched1: Loan 1's payment schedule
        sched2: Loan 2's payment schedule
        title: Overall plot title
    """
    plt.figure(figsize=(10,6))

    plt.subplot(121)
    _plot_loan(sched1)
    plt.grid(True)
    plt.title(title1)

    plt.subplot(122)
    _plot_loan(sched2)
    plt.grid(True)
    plt.title(title2)

    plt.show()


def _format_plot(term_length, max_principal):
    plt.axis([0,term_length, 0,max_principal])
    plt.grid(b=True, which='both', axis='both')
    plt.xlabel("Months")
    plt.ylabel("Dollars")


def _plot(interest, principal, balance, term):
    int_line, = plt.plot(term, interest, 'b', linewidth=1.0)
    int_line.set_label('Total Interest Paid')
    plt.legend()

    princ_line, = plt.plot(term, principal, 'g', linewidth=1.0)
    princ_line.set_label('Total Principal Paid')
    plt.legend()

    bal_line, = plt.plot(term, balance, 'r', linewidth=1.0)
    bal_line.set_label('Total Balance')
    plt.legend()


def _plot_loan(schedule):
    """ Convert a payment schedule into a plottable format. 
    
        An amortization consists of a variety of data points, 
        when graphed over time the data compounds
        to show a trend which can be visualized in a graph.

        Args:
        schedule: A payment schedule
    """
    total_interest_paid = []
    total_principal_paid = []
    balance_remaining = []
    term = []

    total_interest = 0
    total_principal = 0
    for i in range (len(schedule)):
        total_interest += schedule[i][0]
        total_interest_paid.append(total_interest)

        total_principal += schedule[i][1]
        total_principal_paid.append(total_principal)

        balance_remaining.append(schedule[i][2])

        term.append(i)
    
    _plot(total_interest_paid, total_principal_paid, balance_remaining, term)