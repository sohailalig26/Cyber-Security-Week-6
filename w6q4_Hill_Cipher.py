import numpy as np

# Convert letters to numbers
def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    return [ord(char) - ord('A') for char in text]

# Convert numbers back to letters
def numbers_to_text(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

# Encrypt using Hill Cipher
def hill_encrypt(text, key):
    nums = text_to_numbers(text)

    # Padding if odd length
    if len(nums) % 2 != 0:
        nums.append(ord('X') - ord('A'))

    cipher = []

    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(key, pair) % 26
        cipher.extend(result.flatten())

    return numbers_to_text(cipher)

# Decrypt using Hill Cipher
def hill_decrypt(cipher, key):
    det = int(np.linalg.det(key))
    det_inv = pow(det % 26, -1, 26)

    key_inv = det_inv * np.round(det * np.linalg.inv(key)).astype(int) % 26

    nums = text_to_numbers(cipher)
    plain = []

    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(key_inv, pair) % 26
        plain.extend(result.flatten())

    return numbers_to_text(plain)


# Key matrix (must be invertible mod 26)
key = np.array([[3, 3],
                [2, 5]])

# Read plaintext file
with open("plain.txt", "r") as f:
    plaintext = f.read()

ciphertext = hill_encrypt(plaintext, key)

# Save encrypted file
with open("encrypted.txt", "w") as f:
    f.write(ciphertext)

print("Encrypted text:", ciphertext)

# Decrypt the encrypted file
with open("encrypted.txt", "r") as f:
    cipher = f.read()

decrypted = hill_decrypt(cipher, key)

# Save decrypted file
with open("decrypted.txt", "w") as f:
    f.write(decrypted)

print("Decrypted text:", decrypted)