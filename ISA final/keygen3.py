from Crypto.PublicKey import RSA

def export_privatekey(privatekey, filename):
    with open(filename, "wb") as file:
        file.write(privatekey.exportKey('PEM', 'MyPassphrase'))
        file.close()
def export_public_key(public_keyl, filename):
    with open(filename, "wb") as file:
        file.write(public_keyl.exportKey('PEM'))
        file.close()

keypair = RSA.generate(2048)
public_key = keypair.publickey()
export_privatekey(keypair, 'private key.pem')
export_public_key(public_key, 'public_key.pem')