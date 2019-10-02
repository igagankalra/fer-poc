#!/usr/bin/env python

import os
from cryptography.fernet import Fernet
#Reading key from a file after generation.
with open('key1.key', 'rb') as file:
    key = file.read() # The key is type bytes still
print(key)
# file name that has to be Encrypted.
input_file = 'creds.py'
# file name that has to be saved after encryption.
output_file = 'creds.py.enc'


#### Reading file data ####
with open(input_file, 'rb') as f:
    data = f.read()

### Creating object of the Fernet. ###
fernet = Fernet(key)
### Encrypting data with the key(generated before).
encrypted = fernet.encrypt(data)
print(encrypted) # Printing encrypted data.

#### Writing Encrypted file data ####
with open(output_file, 'wb') as f:
    f.write(encrypted)

os.remove('creds.py')

# You can delete input_file if you want