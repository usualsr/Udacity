##i made a change here
##execute with condition
##e.g
n=int(input('enter the value of n \n'))
if (n%2==0):
    print('number ' + str(n)+ ' is even')
else:
    print('odd')

##for more then two possible cases using elif
season=input('enter the season \n')
if season =='winter':
    print('it is cold.always wear warm clothes ')
elif season=='summer':
    print('its hot..use tshirt,glasses and others')
else:
    print('invalid')

##concept of if
phone_balance=4
bank_balance=45
if phone_balance<5:
    phone_balance +=5
    bank_balance -=5
    print(phone_balance)
