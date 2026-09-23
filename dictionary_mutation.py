def add_entry(d): # to add a key-value pair to a dictionary
	"""Prompt for a key and value, then add the pair to ``d``."""
	key = input("Enter key: ")# to prompt the user for a key
	value = input("Enter value: ")# to prompt the user for a value
	d[key] = value # to add the key-value pair to the dictionary
	return d 

    def reassign_dict(d):
	d = {}
	return d
