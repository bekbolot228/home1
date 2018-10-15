from os import remove as delete

old_name = input('Enter the object which you want rename .: ')
new_name = input('Enter the new name of object .: ')

with open(old_name, 'rb') as f:
	f.read()

with open(new_name, 'wb') as f:
	f.write(old_name.read())
delete(old_name)