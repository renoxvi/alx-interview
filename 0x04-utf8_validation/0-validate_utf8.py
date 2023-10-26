def validUTF8(data):
    num_bytes = 0
    for num in data:
        # Check if the number is a single byte character
        if num < 128:
            if num_bytes != 0:
                return False
        else:
            # Count the number of leading '1' bits to determine the byte count
            mask = 1 << 7
            while num & mask:
                num_bytes += 1
                mask >>= 1

            # For multi-byte characters, the next bytes must start with '10'
            if num_bytes == 0 or num_bytes > 3:
                return False
            for i in range(1, num_bytes + 1):
                if i >= len(data) or (data[i] >> 6) != 2:
                    return False
                num_bytes -= 1

        num_bytes = max(num_bytes - 1, 0)

    return num_bytes == 0


# Example usage
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

data3 = [9, 5, 7, 6]
print(validUTF8(data3))  # Output: False
