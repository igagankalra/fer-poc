#!/usr/bin/env python
# This is used to generate the Encryption key based on the common password which is used to encrypt files
# and decrypt them as well.
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#### generating keys according from the password ####

### ***** Provide your password here ***** ####
password_provided = "CHANGE_THIS" # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

### Writing the key into the file. ###
with open('key1.key',  'wb') as file:
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    file.write(key)
    print(key) # Printing key