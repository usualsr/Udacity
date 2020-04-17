
##we can create a list
cities=['ktm','pkr','lamjung','tanahu']
for city in cities:
    print(city)
##also use to create ans modify list
add_city=[]
for x in cities:
    add_city.append(x)
print(add_city)
##to modify a list u need a range():
##range(start,stop,step)
##if u dont specify its..start default to 0 and step defaul to 1
for x in range(0,5,2):
    print(x)
print(list(range(4)))
##calling range with two integer
print(list(range(0,5)))
print(list(range(0,5,2)))
for city in range(2):
    cities[city]=cities[city].title()
    print(cities)