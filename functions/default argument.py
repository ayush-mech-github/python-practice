def user_info(first_name,last_name,age):
    print(f'your first name is {first_name}')
    print(f'your last name is {last_name}')
    print(f'your age is {age}')

user_info('Ayush','Tripathi',21)

#we can choose a default parameter
#default argument should not be after any normal argument.
#value in default argument can be changed by passing an argument to it.

def user_info(first_name,last_name,age=21):
    print(f'your first name is {first_name}')
    print(f'your last name is {last_name}')
    print(f'your age is {age}')

user_info('Ayush','Tripathi',23)
