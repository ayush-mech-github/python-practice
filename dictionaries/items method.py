user={'name':'ayush','age':21,'fav_movies':['shawshank redemption','dangal']}

user_items=user.items()
print(user_items)
print(type(user_items))

for key,value in user.items():
    print(key,value)

for item in user.items():
    print(item)
