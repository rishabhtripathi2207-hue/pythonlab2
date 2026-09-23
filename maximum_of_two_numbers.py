def factorial(n: int) -> int: # to calculate the factorial of a non-negative integer
	"""Return the factorial of a non-negative integer."""# to calculate the factorial of a non-negative integer
	if n < 0: # to check if the input is a negative integer
		raise ValueError("factorial is undefined for negative numbers")# to raise an error for negative integers

	result = 1
	for number in range(2, n + 1): # to iterate through the range of numbers from 2 to n (inclusive)
		result *= number
	return result
