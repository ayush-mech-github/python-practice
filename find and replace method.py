#replace method
string='he is healthy,smart and he plays volleyball'
print(string.replace(' ','_'))
print(string.replace('is','has to be'))
print(string.replace('he','she',1))#replaces one he by she

#find method -used to find position of a character or string
print(string.find('he'))
#we can also mention the position from which search has to begin
he_pos1=string.find('he',)
he_pos2=print(string.find('he',he_pos1+1))
