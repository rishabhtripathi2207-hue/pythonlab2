def change_string(s): # to change the first character of a string
	"""Try to replace the first character and return the new string."""
	if s:       # to check if the string is not empty
		s = "X" + s[1:]
	return s


original = "hello"# TO create a string
changed = change_string(original)# TO call the function and store the result

print("Changed value:", changed)# TO print the changed string
print("Original value:", original)# TO print the original string
print("Original changed:", original != "hello")# TO print whether the original string was changed
