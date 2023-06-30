#looping in tuples
mixed=('ayush',1,2,3,4.0)
for element in mixed:
    print(element)
    

#tuple with one element
#we have to place comma after the element
num=(1,)
word=('A',)
print(type(num))
print(type(word))

#tuple without parenthesis
vegetables='spinach','potatoe','onion'
print(type(vegetables))

#tuple unpacking
footballer=('messi','ronaldo','maradona')
footballer1,footballer2,footballer3=(footballer)
print(footballer1)


#list inside tuples
metro_cities=('india',['it','bangalore'])
metro_cities[1].append('kolkata')
print(metro_cities)
metro_cities[1].pop()
print(metro_cities)

#functions that can be used with tuples
#min(),max(),sum()
mixed=(1,2,3,4.0)
print(min(mixed))
print(max(mixed))
print(sum(mixed))


