ORIGINAL = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

def get_char_code_from_string(string: str) -> int:
	"""
	Convert a string into a 32-bit signed hash value
	"""
	char_code = 0
	if len(string) == 0:
		return char_code
	
	for ch in string:
		code = ord(ch)
		char_code = ((char_code << 5) - char_code) + code
		# ensure 32-bit signed integer behavior
		char_code &= 0xFFFFFFFF
		# convert to signed int like JS bitwise ops
		if char_code & 0x80000000:
			char_code -= 0x100000000
	
	return char_code


def get_char(index: int) -> str:
	"""Return a character from ORIGINAL by index."""
	return ORIGINAL[index]


def generate_string(char_code: int, length: int = 64) -> str:
	"""
	Convert char_code into a string using the ORIGINAL character set.
	"""
	stack = []
	sign = '-' if char_code < 0 else ''
	char_code = abs(char_code)
	
	while char_code >= length:
		index = char_code % length
		char_code = char_code // length
		stack.append(get_char(index))
	
	if char_code > 0:
		stack.append(get_char(char_code))
	
	# reverse stack to build the result
	result = ''.join(reversed(stack))
	return sign + result


def shortener(text: str) -> str:
	"""
	Shorten text using the same algorithm and without before and after spaces.:
		1. Hash text → integer
		2. Encode using ORIGINAL base chars (length=63)
		3. Replace '-' with 'H'
	"""
	shorter = generate_string(get_char_code_from_string(text.strip()), 63)
	return shorter.replace('-', 'H')


# Example usage:
if __name__ == "__main__":
	print(shortener("https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&")) # => 1xWU9E
	print(shortener("     https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&")) # => 1xWU9E
	print(shortener("https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&        ")) # => 1xWU9E
