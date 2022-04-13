from flask import Flask,render_template,request
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
from cryptography.hazmat.primitives import serialization
import os,keygen1,encryptdata,encode,encrypt_image,decrypt_image,decode,decryptdata
#encryptdata,encrypt_image,encode,decrypt_image,decryptdata,decode
app = Flask(__name__)
@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/encrypt/')
def encrypt():
    return render_template('encrypt.html')
@app.route('/encrypt/fg', methods=['POST'])
def encrypt1():
    text=request.form['usertxt']

    keyfile1=request.files['publickey']
    key1path='./keys/public/'+keyfile1.filename
    keyfile1.save(key1path)

    keyfile2=request.files['mainkey']
    key2path='./keys/public/'+keyfile2.filename
    keyfile2.save(key2path)

    keyfile3=request.files['ivkey']
    key3path='./keys/public/'+keyfile3.filename
    keyfile1.save(key3path)

    img=request.files['image1']
    imgpath='./images/encrypted/image.png'
    img.save(imgpath)
    enc=encryptdata.enctext(text)
    encode.Encode(enc)
    filename=r'images\encrypted\encoded.png'
    encrypt_image.encrypt_image(filename)
    



    
    return render_template('index copy 2.html')

@app.route('/decrypt/')
def decrypt():
    return render_template('decrypt.html')
@app.route('/decrypt/gg', methods=['POST'])
def decrypt1():
    

    keyfile1=request.files['privatekey']
    key1path='./keys/public/'+keyfile1.filename
    keyfile1.save(key1path)

    keyfile2=request.files['mainkey']
    key2path='./keys/public/'+keyfile2.filename
    keyfile2.save(key2path)

    keyfile3=request.files['ivkey']
    key3path='./keys/public/'+keyfile3.filename
    keyfile1.save(key3path)

    img=request.files['image2']
    imgpath='./images/decrypted/encrypted.png'
    img.save(imgpath)
    filename=r'images\decrypted\encrypted.png'
    decrypt_image.decryptimage(filename)
    src=r'images\decrypted\decryptedpic.png'
    decdata=decode.Decode(src)
    with open(r"D:\New folder\private.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
    encrypted=bytes(base64.b64decode(decdata))
    original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )

)
    enc1=str(original_message)
    enc1=enc1[1:]
    #print(enc1)
    enc1=enc1[1:]
    #print(enc1)
    enc1=enc1[:-1]
    print(enc1)

    
 
    classification= enc1


    return render_template('index copy 3.html',prediction=classification)

@app.route('/keygen/')
def keygen():
    return render_template('keygen.html')
@app.route('/keygen/hg',methods=['POST'])
def keygenr():
    src=request.form['keyloc']
    keygen1.genkey(src)
    return render_template('index copy.html')
@app.route('/',methods=['POST'])
def goback():
    return render_template('index copy.html')





if __name__ == '__main__':
 app.run(debug='True',port=3000)