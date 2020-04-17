##is used to create a list
fruit=[3,4,5,6,7]
candy=[fruits for fruits in fruit]
print(candy)

##if there is conditon to check(one condition to check)
num=[1,2,3,4,5,6]
check=[nums for nums in num if nums%2==0]
print(check)
##if there is more then one condition to check then

animal=[cat for cat in range(9) if cat%2==0]
print(animal)

##extreact only the first name
names=['ram bahadur','ghun shyam','prem thapa','hari kc']
call=[mero.split()[0].upper() for mero in names]
print(call)
##multiple of 3
mul=[x*3 for x in range(7)]
print(mul)
##filter name by score
name={
    'usual':56,
    'santosh':90,
    'fasical':87
}
for names,score  in name.items():
    if score>60:
        print(names)


sport={
    'usual':90,
    'casual':78,
    'fasical':67
}
new=[name for name,score in sport.items() if score >70]
print(new)