#add data
user_info={'name':'ayush',
           'age':21,
           'fav_movies':['shawshank redemption','dangal']}
user_info['fav_songs']=['song1','song2']
print(user_info)

#pop method ---> remove data
user_info={'name':'ayush',
           'age':21,
           'fav_movies':['shawshank redemption','dangal']}
popped_item=user_info.pop('fav_movies')
print(f'popped item is {popped_item} and new dictionary is {user_info}')
print(type(popped_item))


#popitem method
#randomly removes a key-value pair
user_info={'name':'ayush',
           'age':21,
           'fav_movies':['shawshank redemption','dangal']}
popped_item=user_info.popitem()
print(popped_item)
print(user_info)
print(type(popped_item))
