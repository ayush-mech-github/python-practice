#input dictionary from user and
#print the data in seperate lines


d={}

name=input('enter your name')
age=input('enter your age')
fav_movies=input('enter your favourite movies comma seperated').split(',')
fav_songs=input('enter your favourite songs comma seperated').split(',')

d['name']=name
d['age']=age
d['fav_movies']=fav_movies
d['fav_songs']=fav_songs

for key,value in d.items():
    print(key,value)
