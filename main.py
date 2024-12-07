'''name = 'alexei'
id = 'MD42424242424242'
balance1 = 42
balance2 = 34.2
boolean = False # true
#print(bool(-1))
print('hello ', name)
print('ur ID is ', id)'''
import random

'''score =(int(input('enter your score')))  #score это переменная!!!!!!!!
if score == 50:
    print('you win!')
else:
    print('you need more points ')'''

lives = 3
win_var = random.randint(0, 25)


while lives != 1:
    check = int(input('Enter ur number'))
    if check == win_var:
        print('U win')
        break
    elif check > win_var:
        print('ur number is bigger than need')
    elif check < win_var :
        print("ur number is less than need")
    else:
        print('wrong data input')
    lives = lives - 1
else:
    print("U lose")