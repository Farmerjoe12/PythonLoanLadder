from flask import Flask, render_template, redirect, url_for
from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule
from model.LoanCollection import LoanCollection

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('show_loan'))


@app.route('/loan')
def show_loan():
    l1 = Loan("Tester Loan", 6.05, 15000)
    l2 = Loan("Test loan 2", 5.55, 12000)
    l3 = Loan("Loan 3", 4.23, 19000)
    l4 = Loan("Loan 4", 2.4324, 18385)
    lc = [l1, l2, l3, l4]
    return render_template('loan.html', loans=lc)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
