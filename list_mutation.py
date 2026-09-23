def remove_last(lst): # to remove the last element from a list
	"""Remove and return the last element of lst.""" 
	return lst.pop()


values = [1, 2, 3] # to create a list of integers
removed = remove_last(values)

print(f"Removed: {removed}")# TO print the removed element
print(f"Original list after function call: {values}")# TO print the modified list
