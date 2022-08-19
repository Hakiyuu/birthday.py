birthdays = {'Frank': 'April 28', 'Chinenye': 'july 6', 'Uju': 'May 4', 'Ada': 'june 5'}

while True:
    print('Enter your name')
    name = input()
    if name == 0:
        break
    if name in birthdays:
        print( birthdays[name] + 'is the birthday of' + name)
    else:
        print('i do not have birthday information for ' + name)
        print('When is your birthday')
        birthDay = input()
        print('Birthday Database Updated!')
