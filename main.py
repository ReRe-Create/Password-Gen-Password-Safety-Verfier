import random

#List for possible types of characters

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
'l', 'm', 'n', 'o', 'p', 'q', 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
 'Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

special = ['!','@','#','$','%','^','&','*','(',')','-','+']

#Testing Lists

#print(letters)
#print(numbers)
#print(special)

def pass_generator():
    #Generating random characters
    pw= [ '','','','','','','','','','']

    for i in range (2):
        pw[i] = random.choice(numbers)

    for j in range (5):
        pw[j+2]= random.choice(letters)

    for k in range (3):
        pw[k+7] = random.choice(special)

    #printing password as string
    pws="".join(pw)
    print(pws)

def safe_pass(user_pass, special):
    length = len(user_pass)

    if length <= 8:
        print('The password is too short! It should be more than 8 characters')
        return

    l = any(c.isalpha() for c in user_pass)
    num = any(c.isdigit() for c in user_pass)
    schar = any(c in special for c in user_pass)

    if l and num and schar:
        print('Your password is safe')

    else:
        print('Your password is not safe enough. You should have letters, numbers and special characters')

#Asks users
user_answer = ''
while user_answer != 'a'and user_answer != 'b':
    print('What would you like to use?')
    print('\n (a) Password Generator')
    print('\n (b) Password Safety Verifier\n')
    user_answer = input()

    if user_answer == 'a':
        pass_generator()

    elif user_answer == 'b':
        user_pass= input('Please paste your password: ')
        safe_pass(user_pass, special)

    else:
        print('Please enter (a) or (b)\n')
