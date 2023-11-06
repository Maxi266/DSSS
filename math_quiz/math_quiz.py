import random


def __getRandomInteger(min, max):
    """
    getRandomInteger: Returns a random Integer in Range [min,max] including the endpoints
    """
    return random.randint(min, max)


def __getRandomOperator():
    """
    __getRandomOperator: Returns a random sign to determine wich function to use in the math game
    """
    return random.choice(['+', '-', '*'])


def __getMathOperation(var1, var2, operator):
    """
    getMathOperation: Performs a math operation based on a given Sign and two variables
    Returns the Operation as a String and the answer as an int
    """
    problem = f"{var1} {operator} {var2}"
    if operator == '-': answer = var1 - var2
    elif operator == '+': answer = var1 + var2
    else: answer = var1 * var2
    return problem, answer

def math_quiz(rounds):
    """
    math_quiz: Simple math Game, Give answer to math questions to earn poins over rounds, after finishing the  score is displayed
    """
    score = 0
    roundstoPlay = rounds

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for current_Round in range(roundstoPlay):
        #Get all needed variables to form a simple Math proböem
        var1 = __getRandomInteger(1, 10)
        var2 = __getRandomInteger(1, 5)
        operator = __getRandomOperator()

        problem, answer = __getMathOperation(var1, var2, operator)
        #Display Question as long as there is no valid user input
        while True:
            print(f"\nQuestion {current_Round+13}/{rounds}")
            print(f"Question: {problem}")
            try:
                userAnswer = int(input("Your answer: "))
                break
            except:
                print("You must enter a valid Number (eg. 4) as an answer, not a String")
                print("Please try again")

        if userAnswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{roundstoPlay}")

if __name__ == "__main__":
    #Wait for a valid user Input
    while True:
        try:
            rounds = int(input("How many rounds would you like to play?"))
            break
        except:
            print("You must enter a valid number (eg. 4), not a String")
    math_quiz(rounds)
