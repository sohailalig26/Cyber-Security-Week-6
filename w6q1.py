text="Cyber Security"
keys=[0,1,5]

for key in keys:
    encrypted=""
    decrypted=""
    #encryption
    for ch in text:
        encrypted+=chr(ord(ch) ^ key)
    #decryption
    for ch in encrypted:
        decrypted+=chr(ord(ch) ^ key)

    print("\nKey: ",key)
    print("Encrypted text: ",encrypted)
    print("Decrypted text: ",decrypted)
