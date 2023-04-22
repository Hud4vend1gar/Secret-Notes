import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# # Kullanıcıdan şifreyi girmesini iste
# password = input("Şifreyi girin: ").encode()

# # Rastgele bir salt oluştur
# salt = os.urandom(16)

# # PBKDF2HMAC algoritması ile anahtar türetme
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=480000,
# )
# key = base64.urlsafe_b64encode(kdf.derive(password))
# f = Fernet(key)

# # Şifrelenecek metni kullanıcıdan girmesini iste
# metin = input("Şifrelenecek metni girin: ").encode()

# # Metni şifrele
# token = f.encrypt(metin)
# print("Şifrelenmiş metin: ", token)

# # Şifreyi çöz ve orijinal metni göster

# decrypted_metin = f.decrypt(token).decode()
# print("Çözülmüş metin: ", decrypted_metin)


def encrypt_text(title,secret_note,password):
    #? title
    with open(file="notes.txt",mode="a") as a:
        a.write(title + "\n")

    # Kullanıcıdan şifreyi girmesini iste
    password = password.encode()

    # Rastgele bir salt oluştur
    salt = os.urandom(16)

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

    #? write encrypted text
    with open(file="notes.txt",mode="a") as b:
        token = str(token)
        b.write(token + "\n")

encrypt_text("merhaabaa","çok gizli notumm şş","mypassword")