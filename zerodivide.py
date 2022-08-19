def spam(divideBy):
    try:
       return 42 / divideBy
    except ZeroDivisionError:
        print('error: invalid command')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))  #when code in try clause causes an error ,
                # the program execution moves to except clause, after running the code
                # the execution continues as normal

#try:
    #print(spam(2))
    #print(spam(4))
    #print(spam(0))
    #print(spam(1))
#except ZeroDivisionError:
    #print('error: invalid command')  #when code is executed , spam(1) is never executed because once the execution jumps to the code in the except
    #clause , it does not return to the try clause , instead it continues moving down as normal.

