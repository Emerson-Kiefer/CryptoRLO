import random
from prettytable import PrettyTable

def generate_binary_strings(n):
	if n <= 0:
		return ['']
	previous_strings = generate_binary_strings(n - 1)
	new_strings = [s + '0' for s in previous_strings] + [s + '1' for s in previous_strings]
	return new_strings

def random_bits(length: int):
	"""
    Generate a random binary string of the specified length.

    Parameters:
        length (int): The length of the binary string to generate.

    Returns:
        str: A random binary string of the specified length.
    
    Raises:
        ValueError: If the length is less than or equal to 0.
    """

	if length <= 0:
		raise ValueError("Length must be greater than 0")
	
	bits = [str(random.randint(0,1)) for _ in range(length)]
	return ''.join(bits)

def xor(x1, x2):
	int1 = int(x1, 2)
	int2 = int(x2, 2)

	# XOR operation
	result_int = int1 ^ int2

	# Determine the maximum length of the input binary strings
	max_length = max(len(x1), len(x2))

	# Convert the result back to a binary string with left-padding
	result_str = format(result_int, '0' + str(max_length) + 'b')

	return result_str



def ctr_add(X, i, n):
    decimal_value = int(X, 2)

    decimal_value += i
    result = decimal_value % (2 ** n)

    bin_res = bin(result)[2:].zfill(n) 
    return bin_res

if __name__ == '__main__':
    binary_str = "111"
    i = 2
    n = 3

    result = ctr_add(binary_str, i, n)
    print(result)

