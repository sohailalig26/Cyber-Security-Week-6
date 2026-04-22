def encrypt(text,key):
    res=""
    for ch in text:
        res+=chr(ord(ch)^key)
    return res

txt="Cyber Security"
keys=[0,1,5]

for key in keys:
    encrypted=encrypt(txt,key)
    decrypted=encrypt(encrypted,key)
    
    print("\nKey: ",key)
    print("Encryptyed text: ",encrypted)
    print("Decrypted text: ",decrypted)