fruits=['apple','mangoe','orange','pineapple','banana']
#pop method
fruits.pop()#deletes last element from the list
print(fruits)

fruits=['apple','mangoe','orange','pineapple','banana']
fruits.pop(3)#deletes element at 3rd index
print(fruits)

#del operator
fruits=['apple','mangoe','orange','pineapple','banana']
del fruits[0]
print(fruits)

#remove method
fruits=['apple','mangoe','orange','pineapple','banana']
fruits.remove('mangoe')
print(fruits)

fruits=['apple','mangoe','orange','pineapple','apple','banana']
fruits.remove('apple')#removes first apple
print(fruits)
