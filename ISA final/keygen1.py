from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import os
def genkey(data):
      add1=data+r'\private.pem'
      add2=data+r'\public.pem'
      add3=data+r'\key.txt'
      add4=data+r'\key2.txt'
      private_key = rsa.generate_private_key(
          public_exponent=65537,
          key_size=1024,
          backend=default_backend()
      )
      public_key = private_key.public_key()

      from cryptography.hazmat.primitives import serialization

      private_pem = private_key.private_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PrivateFormat.PKCS8,
          encryption_algorithm=serialization.NoEncryption()
      )
      public_pem = public_key.public_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PublicFormat.SubjectPublicKeyInfo
      )

      with open(add1,'wb') as f:
        f.write(private_pem)
      with open(add2,'wb') as f:
        f.write(public_pem)
      #----------------------------------------Image Encryption key----------------------------------------------------------------------------------------
      keysize=16
      blocksize=16
      def getKey(keysize):
          key=os.urandom(keysize)
          return key
      def getIV(blocksize):
          iv = os.urandom(blocksize)
          return iv
      
      key=getKey(keysize)
      key2=getIV(blocksize)

      with open(add3,'wb') as f:
        f.write(key)
      with open(add4,'wb') as f:
        f.write(key2)

genkey(r'C:\Users\hirwa\OneDrive\Desktop\ISA final\keys')
