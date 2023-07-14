"""Assignment for Git Branch

Purpose: To learn git branch.

Requirement: Jairo and Nina are given a team project to work on together. The project is to create a calculator written in python. 
Nina has built the first version of the project (https://github.com/ninawtt/JairoPractice/blob/main/calculator.py). 
Jairo saw the code and he knows how to make it better. Now what Jairo needs to do is to make the changes by creating a new branch under
the project( Nina's repository. no need to fork). After pushing the code, open the pull request to ask Nina to review and merge the code.

Keywords: git clone, git branch, git checkout, pull request, code review

Estimated Hour: 2 hours"""


def sum(a, b):
    return a + b
while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))

            result = sum(number1, number2)

            print(result)
            break            
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")