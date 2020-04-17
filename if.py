###if is very important
import random

bank_balance=random.randint(500,1000)
print(bank_balance)
phone_balance=int(input('enter the value of your phone'))
if phone_balance<5:
    phone_balance +=10
    bank_balance -=10
    print('your balance is added by 10 and your new amount is ',phone_balance)
    print('and your balance in account is',bank_balance)
else:
    print('you have a balance of',phone_balance)

##
points=int(input('enter the point of user'))
if  points < 15 :
    print('you have won')
if points > 15 and points < 30:
    print('no prize')
if points >= 30 and  points <45 :
    print('nice try')
else:
    print('you are awesome')

    ##
weight=int(input('enter your weight'))
height=int(input('enter your height'))
if weight <60 and height>6 :
    print('you are too skiny')
else:
    balance=weight/height*0.5
    print(balance)
    if balance>1:
        print('you need to improve')
    else:
        print('you are normal')
    if balance>2:
        print('diet as well as exercise')
    else:
        print('only diet ')
        ##loop
  ##  ---allow you to repeat a block of code
fruits=['apple ', 'banana','carrot']
add_fruits=[]
for index in range(len(fruits)):
    fruits[index]=fruits[index].title()
    print(fruits)
game=['football','basketball','volleyball']
for x in range(len(game)):
    game[x]=game[x].title()
    print(game[x])

##while loop
num=[0,2,2,1]
hand=[]
while sum(hand) <=4:
    hand.append(num.pop())
    print(hand)

##for loop
for mul in range(5,35,5):
    print(mul)

##break and continue statement
fruits=[('banana',78),('apple',76),('carrot',23)]
weights=0
for cargo in fruits:
    if weights >=45:
        print()
##
fruits=('apple ','banana','graphes')
for i, fruit in zip(range(len(fruits))):

    ].x/zx../.x/\

              sx8dccs[sxzxuizxZ(i,fruit)