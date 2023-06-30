user={'name':'ayush','age':21}
print(user.get('name'))
print(user.get('sex'))
print(user.get('hobbies','not found !'))

#if two same keys are present
user={'name':'ayush','age':21,'name':'utkarsh'}
print(user.get('name'))#returns last value


