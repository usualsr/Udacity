##zip--to combine iterable we used a zip
game=['football','pubg','pes']
fruits=['apple ','banana','graphes','coconut']
print(list(zip(game,fruits)))

##you can also use a for loop
for games,fruits in zip(game,fruits):
    print(games,fruits)
##we can also unjip
manifest=[('apple',12),('banana',78),('pineapple',45),('mango',56)]
fruits,weight=zip(*manifest)
print(fruits,weight)

##f# for j,item in zip(range(len(fruits))):
print(j,item)