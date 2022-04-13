from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import numpy as np,codecs,base64
from PIL import Image
from cryptography.hazmat.primitives import serialization
# with open("public.pem",'rb') as key_file:
#     public_key = serialization.load_pem_public_key(
#         key_file.read(),
#         backend=default_backend()
#     )




def enctext(message):
    mess=message.encode('utf-8')
    print(mess)
    with open("keys\public\public.pem",'rb') as key_file:
     public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
    
    encrypted = public_key.encrypt(
        mess,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    #print(encrypted)
    enc=str(base64.b64encode(encrypted),'utf-8')
    print(enc)
    print(type(enc))
    return enc
    # print(enc)
    # print(type(enc))
    # enc2=bytes(base64.b64decode(enc))
    # print(enc2)
    # print(type(enc2))
    



# def Encode(img1,message,img2):


#     img = Image.open(img1, 'r')
#     width, height = img.size
#     array = np.array(list(img.getdata()))

#     if img.mode == 'RGB':
#         n = 3
#     elif img.mode == 'RGBA':
#         n = 4
#     total_pixels = array.size//n
#     message += "$t3g0"
#     b_message = ''.join([format(ord(i), "08b") for i in message])
#     req_pixels = len(b_message)
#     if req_pixels > total_pixels:
#      print("ERROR: Need larger file size")

#     else:
#         index=0
#         for p in range(total_pixels):
#             for q in range(0, 3):
#                 if index < req_pixels:
#                     array[p][q] = int(bin(array[p][q])[2:9] + 
# b_message[index], 2)
#                     index += 1
#     array=array.reshape(height, width, n)
#     enc_img = Image.fromarray(array.astype('uint8'), img.mode)
#     enc_img.save(img2)
#     print("Image Encoded Successfully")
# def Stego():
#     print("--Welcome to $t3g0--")
#     print("1: Encode")
#     print("2: Decode")

#     func = input()

#     if func == '1':
#         print("Enter Source Image Path")
#         src = input()
#         print("Enter Message to Hide")
#         message = input()
#         enc=enctext(message)
#         print(enc)
       
#         print("Enter Destination Image Path")
#         dest = input()
#         print("Encoding...")
#         dd=Encode(src, enc, dest)
#         print(dd)
#     else:
#      print("wrong input")

