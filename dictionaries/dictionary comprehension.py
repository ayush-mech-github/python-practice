#square={1:1,2:4,3:9}

square={i:i**2 for i in range(1,11)}
print(square)

square={f'square of {i}':i**2 for i in range(1,11)}
print(square)


#word counter
string=input('enter a string')
word_counter={char:string.count(char) for char in string}
print(word_counter)
