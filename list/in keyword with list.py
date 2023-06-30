#in keyword in list
fruits=['apple','banana','pineapple','orange','mangoe']
if 'orange' in fruits:
    print('orange is present')
else:
    print('orange is not present')


fruits=['apple','banana','pineapple','orange','apple','mangoe']
print(fruits.count('apple'))

#sort method. sorts elements in the list.
fruits=['apple','banana','pineapple','orange','mangoe']
fruits.sort()
print(fruits)

numbers=[6,2,4,6,4,9,1,2]
numbers.sort()
print(numbers)

#sorted function
#original lists remains same
#it just prints the list in sorted order

numbers=[6,2,4,6,4,9,1,2]
print(sorted(numbers))
print(numbers)

#clear method
#empties our list
fruits=['apple','banana','pineapple','orange','mangoe']
fruits.clear()
print(fruits)

#copy method
fruits=['apple','banana','pineapple','orange','mangoe']
fruits1=fruits.copy()
print(fruits1)
