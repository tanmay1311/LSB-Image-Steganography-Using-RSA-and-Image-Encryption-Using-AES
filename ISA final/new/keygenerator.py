import os
import rsa
publicKey, privateKey = rsa.newkeys(512)
print(type(publicKey))
message="dede"

enc=rsa.encrypt(message.encode(),publicKey)
print(enc)
enc1=str(enc)
enc1=enc1[1:]
#print(enc1)
enc1=enc1[1:]
#print(enc1)
enc1=enc1[:-1]
print(enc1)
enc2=enc1.encode('utf-8')
print(enc2)
decMessage = rsa.decrypt(enc2, privateKey).decode()





