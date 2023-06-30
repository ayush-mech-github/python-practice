#in keyword in sets and for loop

s={'a','b','c'}

if 'a' in s:
    print('a is present')
else:
    print('a is not present')

#for loop
for item in s:
    print(item)

#remove duplicate elements in a list
l=[1,2,3,4,4,4,5,6,7,8,8,9]
l1=list(set(l))
print(l1)

#union of two sets
s1={1,2,3,4}
s2={3,4,5,6}
union_set=s1|s2#| ---> pipe
print(union_set)

#intersection of two sets
s1={1,2,3,4}
s2={3,4,5,6}
intersection_set=s1&s2
print(intersection_set)
