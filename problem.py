# if size = 1 then the blocks size will be 4096, if over 4096 then the blocks size will be 2xblock_size etc
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block = filesize % block_size
    # Depending on whether there's a remainder or not, return the right number.
    if filesize < 4096:
        return block_size
    elif partial_block > 0:
        return full_blocks * block_size + block_size    
    return full_blocks * block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192

# Calculate smallest prime factor
def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n += 1

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3
