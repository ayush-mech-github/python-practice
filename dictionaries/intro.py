#data structure
#why we use dictionaries ?
#because of limitations of lists, lists are not enough to represent real
#life data

#example
user=['ayush',21,['shawshank redemption','dangal']]
#user name,age, fav movies
#you can do this but this is not a good way to do this


#dictionaries are un-ordered collection of data
#it means no indexing
#key:value pairs
#dictionaries can store any type of data

user={'name':'ayush','age':21,'fav_movies':['shawshank redemption','dangal']}
print(user)
print(type(user))

#second method to create dictionaries
user1=dict(name='ayush',age=21)
print(user1)

#data is accessed in a dictionary using its key
user={'name':'ayush','age':21,'fav_movies':['shawshank redemption','dangal']}
print(user['name'])
print(user['age'])
print(user['fav movies'])


#how to add data to a dictionary
user1={}
user1['name']='ayush'
user1['age']=21
user1['fav_movies']=['shawshank redemption','dangal']
print(user1)
