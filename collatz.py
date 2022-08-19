#Project
#projectname _ The collatz


def collatz(number):
    while number != 1:

        if number % 2 == 0:
            number = (number // 2)
            print(number)
        elif number % 2 != 0:
            number = 3 * number + 1
            print(number)

try:
    print("Enter your number: ")
    num = int(input())
    collatz(num)
except ValueError:
    print("Invalid. please use an integar.")






