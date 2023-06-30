nums=list(range(1,11))

#create a new list
#if odd ---> multiply by -1
#if even --->multiply by 2

new_list=[i*2 if i%2==0 else -i for i in nums]
print(new_list)

