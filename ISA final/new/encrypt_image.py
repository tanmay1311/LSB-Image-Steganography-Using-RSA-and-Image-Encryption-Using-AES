import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
def getKey(keysize):
    key=os.urandom(keysize)
    return key
def getIV(blocksize):
    iv = os.urandom(blocksize)
    return iv
file = open(r"C:\Users\hirwa\OneDrive\Desktop\ISA final\keys\private\key.txt", "rb")
key1=file.read()
file = open(r"C:\Users\hirwa\OneDrive\Desktop\ISA final\keys\private\key2.txt", "rb")
key2=file.read()

def encrypt_image(filename):
    BLOCKSIZE = 16
    encrypted_filename = filename
    with open(filename, "rb") as filel:
        data = filel.read()
        cipher = AES.new(key1, AES.MODE_CBC, key2)
        ciphertext = cipher.encrypt(pad(data, BLOCKSIZE))

        with open(encrypted_filename, "wb") as file2:
            file2.write(ciphertext)

    return encrypted_filename



filename="images\encrypted\encodedpic.png"

gg=encrypt_image(filename)
print("done")



