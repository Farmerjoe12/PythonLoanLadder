from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

""" A Repayment Schedule can be viewed convieniently in a graph format.

    The graph shows the amounts paid to interest and principal over time,
    as well as the principal remaining throughout the term.
"""
class AmortizationView(FigureCanvas):

    def __init__(self, payment_schedule, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self._sched = payment_schedule
        self.plot("Title")

        
    def plot(self, title):
        plt.title(title)
        self._plot_loan(self._sched)
        plt.grid(True)
        self.draw()


    def plot_on_window(self, title):
        plt.title(title)
        self._plot_loan(self._sched)
        plt.grid(True)
        self.draw()


    def plot_single_payment_sched(self, schedule, title):
        """ View the payment schedule of a single loan in graph format.

            Args:
            schedule: The payment schedule of a loan
        """
        plt.title(title)
        self._plot_loan(schedule)
        plt.grid(True)
        plt.show()


    def plot_two_payment_sched(self, sched1, title1, sched2, title2):
        """ Plot two payment schedules side by side:

            Args:
            sched1: Loan 1's payment schedule
            sched2: Loan 2's payment schedule
            title: Overall plot title
        """
        plt.figure(figsize=(10,6))

        plt.subplot(121)
        self._plot_loan(sched1)
        plt.grid(True)
        plt.title(title1)

        plt.subplot(122)
        self._plot_loan(sched2)
        plt.grid(True)
        plt.title(title2)

        plt.show()


    def _format_plot(self, term_length, max_principal):
        plt.axis([0,term_length, 0,max_principal])
        plt.grid(b=True, which='both', axis='both')
        plt.xlabel("Months")
        plt.ylabel("Dollars")


    def _plot(self, interest, principal, balance, term):
        ax = self.figure.add_subplot(111)
        ax.plot(term, interest, 'b', linewidth=1.0, label = "interest")

        ax.plot(term, principal, 'g', linewidth=1.0, label = "principal")

        ax.plot(term, balance, 'r', linewidth=1.0, label = "balance")
        ax.grid(True)
        ax.legend(("interest", "principal", "balance"), loc='upper right')


    def _plot_loan(self, schedule):
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
        
        self._plot(total_interest_paid, total_principal_paid, balance_remaining, term)