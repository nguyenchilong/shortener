ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
BASE = len(ALPHABET)

"""
Base-64 Short Code Table
----
| Code Length
 | Possible Codes (64^L) | Max URLs (~1% collision risk) |
| ----------- | --------------------- | ----------------------------- |
| 4           | 16,777,216            | ~1,830                        |
| 5           | 1,073,741,824         | ~146,000                      |
| 6           | 68,719,476,736        | ~1,170,000                    |
| 7           | 4,398,046,511,104     | ~8,000,000                    |
| 8           | 281,474,976,710,656   | ~53,000,000                   |

"""
def total_codes(length: int, base: int = BASE):
    return base ** length


# ---------------------------
# 1. Original 32-bit hash
# ---------------------------
def get_char_code_from_string(string: str) -> int:
	char_code = 0
	if not string:
		return char_code
	
	for ch in string:
		char_code = ((char_code << 5) - char_code) + ord(ch)
		# 32-bit boundary
		char_code &= 0xFFFFFFFF
		
		# convert to signed 32-bit
		if char_code & 0x80000000:
			char_code -= 0x100000000
	
	return char_code


# ---------------------------
# 2. Encode integer → fixed-length base-64 string
# ---------------------------
def encode_base_n(num: int, length: int, alphabet: str = ALPHABET) -> str:
	base = len(alphabet)
	arr = []
	
	for _ in range(length):
		arr.append(alphabet[num % base])
		num //= base
	
	# reverse because digits are built backwards
	return "".join(reversed(arr))


# ---------------------------
# 3. Generate forced-length base-64 short code
# ---------------------------
def shortener(url: str, length: int = 6) -> str:
	url = url.strip()
	
	# Hash input
	h = abs(get_char_code_from_string(url))
	
	# Force the hashed value to exactly N base-64 digits
	max_value = BASE ** length
	h_mod = h % max_value
	
	# Encode forced hash into a fixed-length base-64 string
	return encode_base_n(h_mod, length)


# Example usage:
if __name__ == "__main__":
	length = 6
	print(total_codes(length=length))
# print(shortener("https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&")) # => 1xWU9E
# print(shortener("     https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&")) # => 1xWU9E
# print(shortener("https://www.afternic.com/forsale/kpt.ai?utm_source=TDFS_DASLNC&utm_medium=parkedpages&utm_campaign=x_corp_tdfs-daslnc_base&traffic_type=TDFS_DASLNC&traffic_id=daslnc&        ")) # => 1xWU9E
