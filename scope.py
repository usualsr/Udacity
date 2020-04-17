egg_count=12
def buy_egg():
    print('the value of egg is',egg_count)


buy_egg()

##
egg_count = 0
##
def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(buy_eggs(7))