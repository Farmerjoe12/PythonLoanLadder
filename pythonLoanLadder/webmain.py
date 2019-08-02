from flask import Flask, render_template
from model.Loan import Loan
from model.RepaymentSchedule import RepaymentSchedule
from model.LoanCollection import LoanCollection

app = Flask(__name__)


@app.route('/')
def hello_world():
    out = 'Hello World!\n'
    out += 'Open the URL in another tab and go to /hello/yourname'
    return out


@app.route('/loan')
def show_loan():
    # result = "<body"
    # result += "<h1>Loan info viewer</h1>"
    l1 = Loan("Tester Loan", 6.05, 15000)
    l2 = Loan("Test loan 2", 5.55, 12000)
    l3 = Loan("Loan 3", 4.23, 19000)
    l4 = Loan("Loan 4", 2.4324, 18385)
    lc = [l1, l2, l3, l4]
    # result += lc.to_html()
    # result += "</body>"
    return render_template('loan.html', loans=lc)


@app.route('/test')
def test():
    return 'Test'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name + '!'


if __name__ == '__main__':
    app.run(host='127.0.0.1')
