# Encrypt

print("In order to use the code press e - Encryption, d - Decryption")
b = input("Enter your option: ")
if b == 'e':
    message = input("Enter your message: ")
    print("Cipher text: ", end=""),
    for i in message:
        a = ord(i)+3
        print(chr(a),end=""),
elif b == 'd':
    cipher = input("Enter cipher: ")
    print("Message: ",end=""),
    for j in cipher:
        d = ord(j)-3
        print(chr(d),end=""),