import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# password = b"password"
# salt = bytes(16)
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=480000,
# )
# key = base64.urlsafe_b64encode(kdf.derive(password))
# f = Fernet(key)
# a = bytes(b"gAAAAABkREQQI7MgvAfc2nYXrA-sOPTiF3UbNk5FjtaOqmnmqi1AL-droMAeiQGar2tnfjpqVE_a0DetF2HFN2z6cfELmd2R3Q==")
# print(f.decrypt(a))


#* encrypt func
def encrypt_text(title,secret_note,password_input):
    #? title
    with open(file="notes.txt",mode="a") as a:
        a.write(title + "\n")

    def encrypt():
        # Kullanıcıdan şifreyi girmesini iste
        password = password_input.encode()
        # Rastgele bir salt oluştur
        salt = bytes(16)
        # PBKDF2HMAC algoritması ile anahtar türetme
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        f = Fernet(key)
        # Şifrelenecek metni kullanıcıdan girmesini iste
        metin = secret_note.encode()
        # Metni şifrele
        token = f.encrypt(metin)
        token = str(token)
        return token

    #? write encrypted text
    with open(file="notes.txt",mode="a") as b:
        b.write(encrypt() + "\n \n")


#* decrypt func
def decrypt_text(secret_note,password_input):

    password = password_input.encode()
    salt = bytes(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    a = bytes(secret_note.encode())
    return f.decrypt(a)

