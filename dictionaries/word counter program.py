#a key is not repeated in a dictionary
d={'a':1,'b':2,'c':3,'a':3}
print(d)#last a will win

def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count

string=input('enter a string')
print(word_counter(string))
