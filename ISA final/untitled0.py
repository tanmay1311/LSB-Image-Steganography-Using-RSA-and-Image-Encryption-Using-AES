
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import base64
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

with open('private.pem','wb') as f:
  f.write(private_pem)
with open('public.pem','wb') as f:
  f.write(public_pem)

with open("private.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
with open("public.pem",'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

message=input('enter: ')
mss=message.encode('utf-8')
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
encrypted = public_key.encrypt(
    mss,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(encrypted)

encrypted=str(base64.b64encode(encrypted),'utf-8')
print(encrypted)
encrypted=bytes(base64.b64decode(encrypted))

original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)

