from decryptdata import dectext
from encode import Encode
import encryptdata,decode,decryptdata
#import decode,decrypt_image,encode,encrypt_image,decryptdata
# data=input('enter data: ')
# data=data.encode('utf-8')
# enc=encryptdata.enctext(data)
# print(enc)
# src=input('enter data: ')
# dst=input('enter data: ')
# Encode(src,enc,dst)
dst1=input('enter data: ')
enc1=decode.Decode(dst1)
dd=decryptdata.dectext(enc1)
dd1=str(dd)
print(dd1)
