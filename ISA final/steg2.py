import numpy as np,codecs
from PIL import Image
import os
import rsa
publicKey, privateKey = rsa.newkeys(512)


def Encode(message):

    img1="images\encrypted\image.jpg"
    img2="images\encrypted\encodedpic.png"
    img = Image.open(img1, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    message += bytes('*****',encoding='utf8')
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)
    if req_pixels > total_pixels:
     print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + 
b_message[index], 2)
                    index += 1
    array=array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save(img2)
    print("Image Encoded Successfully")
def Decode():
    img3="images\decrypted\decryptedpic.png"
    img = Image.open(img3, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "*****":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "*****" in message:
        print("Hidden Message:", message[:-5])
        
    else:
        print("No Hidden Message Found")
def Stego():
    print("--Welcome to $t3g0--")
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        
        
        message = input()
        enc=rsa.encrypt(message.encode(),publicKey)
        print("Encoding...")
        Encode(enc)

    elif func == '2':
        
        print("Decoding...")
        Decode()

    else:
        print("ERROR: Invalid option chosen")
Stego()
     

