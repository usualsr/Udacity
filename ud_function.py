def cylinder_volume(height,radius=5):
    pi=3.149      ##this pi is a local variable and it cannot be access outside the function
    return height*pi*radius**2
print(cylinder_volume(10,9))
def math():
 pi=3.14
 sum=87*pi
 return sum
print(math())

##
def population_density(population,landarea):
    density=population/landarea
    return density
print(population_density(10,1))
print(population_density(864816,121.4))

def readable_timedelta(days):
    week=days//7
    day=days%7
    return '{} week and {} day'.format(week,day)
print(readable_timedelta(23))