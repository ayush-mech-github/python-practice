# to remove spaces in a string
# lstrip() method removes left spaces
# rstrip() method removes right spaces
# strip() removes both left and right spaces
name = '     ayush    '
dots = '......'
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)


# to remove spaces present between the string
name = 'ayu   sh'
# replace() method is used
print(name.replace(' ', ''))
print(name.replace(' ', '')+dots)
