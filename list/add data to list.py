#it is the most common and most important thing you can do with your list.
#done by using append() method
#it adds item at last position
fruits=['grapes','apples']
fruits.append('mangoes')
print(fruits)

#insert method adds element at desired index
#list.insert(index,element)
fruits1=['oranges','apples']
fruits1.insert(1,'banana')
fruits1.insert(10,'pomogranate')#pomogranate will be added at last index
print(fruits1)

#concatenation of two strings
fruits1=['oranges','apples']
fruits=['grapes','apples']
fruits3=fruits1+fruits
print(fruits3)
#concatenation of two strings by extend method
fruits1=['oranges','apples']
fruits=['grapes','apples']
fruits.extend(fruits1)
print(fruits)

#list in another list
fruits1=['oranges','apples']
fruits=['grapes','apples']
fruits.append(fruits1)#this will append whole list of fruits 1 in fruits.


