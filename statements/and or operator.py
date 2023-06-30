#check two conditions at the same time.
#and , or

age=int(input('enter your age'))
if age>=13 and age<=19:
    print('you are a teenager')
else:
    print('you are not a teenager')


age=int(input('enter your age'))
if age<13 or age>19:
    print('you are not teenager')
else:
    print('you are a teenager')
