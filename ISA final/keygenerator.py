import os
import rsa,base64
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
enc2=str(base64.b64encode(enc),'utf-8')

print(enc2)
print(type(enc2))
enc3=bytes(base64.b64decode(enc2))
print(enc3)


decMessage = rsa.decrypt(enc3, privateKey).decode()
print(decMessage)





