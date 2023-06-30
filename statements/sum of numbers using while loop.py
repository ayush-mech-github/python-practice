minimum,maximum=input('enter minimum and maximum number').split()
minimum=int(minimum)
maximum=int(maximum)
total=0
i=minimum
while i<=maximum:
    total=total+i
    i=i+1
print(f'sum is {total}')
