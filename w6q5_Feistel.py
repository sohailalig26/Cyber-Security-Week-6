# Round function
def F(right, key):
    return right ^ key   # XOR operation


# Feistel Encryption
def feistel_encrypt(left, right, keys, rounds):
    print("Initial Left =", left, "Right =", right)

    for i in range(rounds):
        temp = right
        right = left ^ F(right, keys[i])
        left = temp

        print(f"Round {i+1} -> Left = {left}, Right = {right}")

    print("Cipher Text:", (left, right))


# Main program
left = int(input("Enter left half of plaintext: "))
right = int(input("Enter right half of plaintext: "))

keys = [5, 7, 3, 9]   # Example round keys
rounds = len(keys)

feistel_encrypt(left, right, keys, rounds)