import unittest
from model.Loan import Loan

class Loan_test(unittest.TestCase):
    

    def test_to_string(self):
        target = Loan("Loan 0666", 6.66, 15000)
        expected = "Loan Name: {}\nPrincipal: {}\n".format("Loan 0666", 15000)
        expected += "Interest Rate: %{}".format(6.66)
        self.assertEqual(expected, target.to_string())

            
if __name__ == '__main__':
    unittest.main()