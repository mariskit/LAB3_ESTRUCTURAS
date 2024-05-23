
from Crypto.Hash import SHA3_512

user='danielhoyos'
salt = "d10fc51de79fb0cf2c01b3e7597eec40"
pwd = '34a08e6d888b31663c5886475d2297e912b671e0c6afe94a080f5216138de0bb0115016ff3aaf55eddc816858f53d913e3ec7330936beccfd9f7427ec92692f8'

salt_b = bytes.fromhex(salt)

# Path to the rockyou.txt file
rockyou_path = 'rockyou.txt'
possible_passwords = []
with open(rockyou_path, 'r', encoding='latin-1') as file:
    possible_passwords = [line.strip() for line in file]

for password in possible_passwords:
    print(password)

for password in possible_passwords:
    for pepper in range(256):
        H=SHA3_512.new()
        password_b=bytes(password, 'utf-8')
        H.update(password_b)
        
        pepper_b=pepper.to_bytes(1, 'big')
        H.update(pepper_b)
        
        salt_b=bytes.fromhex(salt)
        H.update(salt_b)
        
        pwd_h=H.hexdigest()
        
        if pwd == pwd_h:
            print(password)
            break