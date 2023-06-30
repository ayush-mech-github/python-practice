#we can create a list in one line

#create a list of squares from 1 to 10
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

square2=[i**2 for i in range(1,11)]
print(square2)

#create a list of negative numbers from 1 to 10
negative_num=[]
for i in range(1,11):
    negative_num.append(-i)
print(negative_num)

negative_num2=[-i for i in range(1,11)]
print(negative_num)

#names=['ayush','himanshu']
#new_list=['a','h']
names=['ayush','himanshu']
new_list=[]
for element in names:
    new_list.append(element[0])
print(new_list)

new_list1=[element[0] for element in names]
print(new_list)    
   
    
