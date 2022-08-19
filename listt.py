#import random

#messages = ['it is certain',
            #'it is decidely so',
            #'yes definately',
            #'reply hazy try again',
            #'ask again later',
            #'concentrate and ask again',
            #'my reply is no',
            #'outlook not so good',
            #'very doubtful',]

#print(messages[random.randint(0, len(messages)-1)])

#name = 'Zophie a cat'
#newName = name[0:7] + 'the' + name[8:12]   #mutating a string using slicing and concatenation
#print(newName)

#eggs = ('hello', 42 , 0.5)
#print(eggs[0])
#print(eggs[1:3])

#print(type(('hello',)))   #tuple - immutable , value doesn't change .
                          #tuple- slighty faster code run

#def eggs(someParameter):
    #someParameter.append('Hello')

#spam = [1,2,3]
#eggs(spam)
#print(spam)

#import copy
#spam = ['A', 'B', 'C', 'D']
#cheese = copy.copy(spam)     #This allows you make a duplicate copy of mutable values
                            # like list or dictionaries copy.copy()
#cheese[1] = 42
#print(spam)
#print(cheese)


