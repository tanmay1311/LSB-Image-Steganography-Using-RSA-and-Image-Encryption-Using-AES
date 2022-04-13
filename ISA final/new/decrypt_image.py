import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
file = open(r"C:\Users\hirwa\OneDrive\Desktop\ISA final\keys\private\key.txt", "rb")
key1=file.read()
file = open(r"C:\Users\hirwa\OneDrive\Desktop\ISA final\keys\private\key2.txt", "rb")
key2=file.read()
img1=r'images\decrypted\decryptedpic.png' 
filename="images\encrypted\encodedpic.png"
def decryptimage(filename):
    BLOCKSIZE = 16
    decrypted_filename = filename
    with open(filename, "rb") as filel:
        data = filel.read()
        cipher2 = AES.new(key1, AES.MODE_CBC, key2)
        decrypted_data = unpad(cipher2.decrypt(data), BLOCKSIZE)
        with open(img1, "wb") as file2:
            file2.write(decrypted_data)
    return decrypted_filename
decryptimage(filename)
print('done')






