#!/usr/bin/env python

from cryptography.fernet import Fernet
#Reading key from a file after generation.
with open('key1.key', 'rb') as file:
    key = file.read() # The key is type bytes still
print(key) #printing Key

# Encrypted file that has to be Decrypted.
input_file = 'creds.py.enc'
# Decrypted file name that has to be save after decryption.
output_file = 'creds.py'

#Readng Encrypted data.
with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
#Decrypting the Encrypted data.
decrypted = fernet.decrypt(data)

#Writing decrypted data to the file.
with open(output_file, 'wb') as f:
    f.write(decrypted)

# You can delete input_file if you want