# define a function that takes a string as input and
# returns True if it is palindrome, otherwise False.

def is_palindrome(string1):
    reverse_string = string1[::-1]
    if string1 == reverse_string:
        return True
    return False


string = input('enter a string ')
print(is_palindrome(string))
