numbers=list(range(1,11))

#make a list that contains even numbers from the above list

even_num=[]
odd_num=[]
for element in numbers:
    if element%2==0:
        even_num.append(element)
    else:
        odd_num.append(element)
print(even_num,odd_num)


even_num2=[i for i in numbers if i%2==0]
odd_num
2=[i for i in numbers if i%2!=0]
print(even_num2)
print(odd_num2)
