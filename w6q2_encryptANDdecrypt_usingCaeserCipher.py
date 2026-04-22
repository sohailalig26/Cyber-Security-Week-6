def encrypt(text, key):
    res=""
    for char in text:
        if char.isalpha():
            shift=ord(char) + key #ord(): character to ASCII value
            res+=chr(shift)       #chr(): ASCII value to character
        else:
            res+=char
    return res

def decrypt(cipher, key):
    res=""
    for char in cipher:
        if char.isalpha():
            shift=ord(char) - key
            res+=chr(shift)
        else:
            res+=char
    return res

txt=input("Enter text to be encrypteed: ")
k=int(input("Enter key: "))

encrypted=encrypt(txt,k)
print("Encrypted text: ",encrypted)

decrypted=decrypt(encrypted,k)
print("Decrypted text: ",decrypted)