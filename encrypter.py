from Crypto.Hash import SHA3_512
from Crypto.Random import get_random_bytes

#Para pruebas
user='danielhoyos'
password="111111"

H=SHA3_512.new()

password_b=bytes(password, "utf-8")
H.update(password_b)
pepper=get_random_bytes(1)
H.update(pepper)
salt=get_random_bytes(16)
H.update(salt)
pdw=H.hexdigest()
print(user)
print(salt.hex())
print(pdw)