# first home work

# part 1 with out 'with'
filename = input('Please, type file name you want to create: ')
text = input('Please, type the text you want to write: ')

file = open(filename, 'w')
file.write(text)
print('There are ' + str(len(text)) + ' symbols ')

file.close()

# part 2 with use 'with'
filename = input('Please, type file name you want create: ')
text = input('Please, type the text you want to write: ')

with open(filename, 'w') as f:
    f.write(text)
        
print('There are ' + str(len(text)) + ' symbols ')


# second home work

# part 1 with out 'with'
filename1 = input('Enter the name of the file you want to copy.: ')
filename2 = input('Enter the name of the file you want to create.: ')
text = input('Please, type the text you want to write in create file: ')

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')
file = open(filename2, 'w')

file.write(text)
text = file1.read()
file2.write(text)

print(filename2.read())

file1.close()
file2.close()
file.close()

# part 2 with use 'with'

filename1 = input('Enter the name of the file you want to copy.: ')
filename2 = input('Enter the name of the file you want to create.: ')
text = input('Please, type the text you want to write: ')

with open(filename1, 'rb') as f:
	f.read()
with open(filename2, 'w') as f:
	f.write(text)
with open(text, 'w') as f:
    f.write(text)


# third home work

# part 1 with out 'with'

from os import remove as delete

old_name = input('Enter the object which you want rename .: ')
new_name = input('Enter the new name of object .: ')

old_name2 = open(old_name, 'rb')
new_name2 = open(new_name, 'wb')

new_name2.write(old_name.read())
old_name2.close()
delete(old_name)
new_name2.close()

# part 2 with use 'with'

from os import remove as delete

old_name = input('Enter the object which you want rename .: ')
new_name = input('Enter the new name of object .: ')

with open(old_name, 'rb') as f:
	f.read()

with open(new_name, 'wb') as f:
	f.write(old_name.read())
delete(old_name)