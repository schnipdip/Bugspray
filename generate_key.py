from cryptography.fernet import Fernet
import os

def generate_key():
    
    #Generates a key and save it into a file
    key = Fernet.generate_key()

    if os.path.isfile('secret.key'):
        pass
    else:
        with open('secret.key', 'w+') as key_file:
            pass
    
    if os.stat('secret.key').st_size == 0:
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
    else:
        print ('Key already exits. If you want to generate a new key delete the key in the secrets.key file.')
        exit(0)
            

generate_key()