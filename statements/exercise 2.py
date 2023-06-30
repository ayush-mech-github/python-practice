#EXERCISE WATCH ADULT MOVIE.
#ask user's name and age.
#if user's name starts with ('a' or 'A') and age is above 10 then
#print 'you can wath adult movie'
#else, print 'sorry, you cannot watch coco movie'

name,age=input('enter your name and age').split(',')
age=int(age)
if (name[0]=='a' or name[0]=='A') and age>10:
    print('you can watch adult movie')
else:
    print('sorry you cannot watch adult movie')
