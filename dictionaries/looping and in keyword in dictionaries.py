user={'name':'ayush','age':21,'fav_movies':['shawshank redemption','dangal']}

#check if key is present in the dictionary
if 'name' in user:
    print(True)
else:
    print(False)

#check if value is present in the dictionary ----> values method
if 'ayush' in user.values():
    print(True)
else:
    print(False)

#loops in dictionaries
for key in user:
    print(key)

for value in user.values():
    print(value)

for value in user:
    print(user[value])

#values method
user_values=user.values()
print(user_values)
print(type(user_values))

#keys method
user_keys=user.keys()
print(user_keys)
print(type(user_keys))


