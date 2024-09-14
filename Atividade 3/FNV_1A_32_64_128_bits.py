def fnv1a_hash_32(text: str, seed: int = 0x811c9dc5) -> int:
    """
    Calculate the 32-bit FNV-1a hash for a given text.

    Parameters:
    - text: The input text to hash.
    - seed: The initial hash value. Default is the FNV offset basis.

    Returns:
    - The 32-bit FNV-1a hash of the input text.
    """
    fnv_prime = 0x01000193
    hash_value = seed

    text_bytes = text.encode('utf-8')

    for byte in text_bytes:
        hash_value ^= byte
        hash_value *= fnv_prime
        hash_value &= 0xffffffff  # Ensure hash_value is a 32-bit number

    return hash_value


def fnv1a_hash_64(text: str, seed: int = 0xcbf29ce484222325) -> int:
    """
    Calculate the 64-bit FNV-1a hash for a given text.

    Parameters:
    - text: The input text to hash.
    - seed: The initial hash value. Default is the FNV offset basis.

    Returns:
    - The 64-bit FNV-1a hash of the input text.
    """
    fnv_prime = 0x100000001b3
    hash_value = seed

    text_bytes = text.encode('utf-8')

    for byte in text_bytes:
        hash_value ^= byte
        hash_value *= fnv_prime
        hash_value &= 0xffffffffffffffff  # Ensure hash_value is a 64-bit number

    return hash_value


def fnv1a_hash_128(text: str, seed: int = 0x6c62272e07bb014262b821756295c58d) -> int:
    """
    Calculate the 128-bit FNV-1a hash for a given text.

    Parameters:
    - text: The input text to hash.
    - seed: The initial hash value. Default is the FNV offset basis.

    Returns:
    - The 128-bit FNV-1a hash of the input text.
    """
    fnv_prime = 0x1000000000000000000013b
    hash_value = seed

    text_bytes = text.encode('utf-8')

    for byte in text_bytes:
        hash_value ^= byte
        hash_value *= fnv_prime
        hash_value &= 0xffffffffffffffffffffffffffffffff  # Ensure hash_value is a 128-bit number

    return hash_value

# Example usage
text = "Hello, World!"
hash_value_32 = fnv1a_hash_32(text)
hash_value_64 = fnv1a_hash_64(text)
hash_value_128 = fnv1a_hash_128(text)

print(f"FNV-1a 32-bit hash of '{text}' is: {hash_value_32:#010x}")
print(f"FNV-1a 64-bit hash of '{text}' is: {hash_value_64:#018x}")
print(f"FNV-1a 128-bit hash of '{text}' is: {hash_value_128:#034x}")
