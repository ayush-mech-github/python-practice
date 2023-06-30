#fromkeys method
#used to creat dictionary having keys with default values

d=dict.fromkeys(['name','age','height'],'unknown')
print(d)

d=dict.fromkeys(('name','age','height'),'unknown')
print(d)

d=dict.fromkeys('abc','unknown')
print(d)

d=dict.fromkeys(range(1,11),'unknown')
print(d)

d=dict.fromkeys(['name','branch'],['unknown','unknown'])
print(d)


#get method
d={'name':['ayush','amit'],'age':[21,19]}
print(d.get('name'))
print(d.get('sex'))#returns none

#clear method
d={'name':['ayush','amit'],'age':[21,19]}
d.clear()
print(d)

#copy method
d={'name':['ayush','amit'],'age':[21,19]}
d1=d.copy()
print(d1)

print(d1 is d)
print(d1 == d)







