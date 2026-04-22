def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = []

    # Add key letters first
    for letter in key:
        if letter not in used and letter.isalpha():
            used.append(letter)

    # Add remaining alphabet letters
    for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letter not in used:
            used.append(letter)

    # Create 5x5 matrix
    for i in range(0, 25, 5):
        matrix.append(used[i:i+5])

    return matrix


def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = ""

        if i + 1 < len(text):
            b = text[i+1]

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            if b:
                pairs.append(a + b)
                i += 2
            else:
                pairs.append(a + "X")
                i += 1

    return pairs


def encrypt(matrix, text):
    pairs = prepare_text(text)
    cipher = ""

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        # Same row
        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        # Rectangle rule
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt(matrix, text):
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    plain = ""

    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        # Same row
        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]

        # Rectangle rule
        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


# Main Program
key = input("Enter key: ")
matrix = create_matrix(key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(row)

choice = input("\nEnter E to Encrypt or D to Decrypt: ").upper()

if choice == "E":
    text = input("Enter plaintext: ")
    print("Ciphertext:", encrypt(matrix, text))

elif choice == "D":
    text = input("Enter ciphertext: ")
    print("Decrypted text:", decrypt(matrix, text))