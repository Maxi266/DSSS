import unittest
from math_quiz import getRandomInteger,getRandomOperator, getMathOperation


class TestMathGame(unittest.TestCase):

    def test_getRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getRandomOperator(self):
        #Test if random signs are generated properly
        for _ in range(1000):
            random_Sign = getRandomOperator()
            self.assertTrue(random_Sign in {"+","-","*"})
        pass

    def test_getMathOperation(self):
            #Test if the Math Operation is performed properly and the expected outputs match
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 7,  "*","4 * 7",28),
                (5, 9,  "-","5 - 9",-4),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                givenProblem, givenAnswer = getMathOperation(num1,num2,operator)
                self.assertTrue(givenProblem == expected_problem and givenAnswer == expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
