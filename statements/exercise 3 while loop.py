#ask user for a natural number.print sum from 1 to n.
num=int(input('enter a number'))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(f'sum from 1 to {num} is {sum}')

#ask use to enter a number and print sum of digits of the number.
num=int(input('enter a number '))
total=0
while i>0: 
  i=num%10
  num=num//10
  total=total+i

print(f'sum of digits is {total}')

                               #OR by using index
num=input('enter a number ')
total=0
i=0
while i<len(num):#not = because indexing is 1 less than length.
  total=total+int(num[i])
  i+=1
print(f'sum of digits is {total}')


