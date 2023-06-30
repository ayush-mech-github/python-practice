#unordered collection of unique items
#dictionary, tuple,list cannot be stored in a set

s={1,2,3,4,4,5,6,6,7}
print(s)

#remove repeated elements
l=[1,1,2,2,3,4,5,6,7,7,7,8]
s2=list(set(l))
print(s2)

#add an element to set
s={1,2,3,4}
s.add(5)
print(s)

#remove an element from set --->remove method,discard method
s={1,2,3,4}
s.remove(3)
print(s)

s={1,2,3,4}
s.discard(3)
s.discard(5)
print(s)

#to clear the set
s={1,2,3,4}
s.clear()
print(s)

#to copy a set
s={1,2,3,4}
s1=s.copy()
print(s1)
print(s1 is s)
print(s1 == s)
