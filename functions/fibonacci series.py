def fibonacci(n):
    i,a,b=1,-1,1
    while i<=n:
        c=a+b
        print(c,end=" ")#by default, it is \n
        a,b=b,c
        i=i+1

num=int(input('enter the number of terms in the fibonacci series '))
fibonacci(num)

#1,2,3,5,8,13,...
#a=1,b=2,c=a+b
