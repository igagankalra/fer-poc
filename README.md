# fer-poc

It uses Microsoft Cognative API to predict the emotions.

## Contributing/Using

There are 2 ways to use this repo,

1st -- You can create your own creds.py file after cloning this repo. Once creds file is created, define your KEY and ENDPOINT for cognative API into it.


2nd -- You can use our creds.py and our KEY & ENDPOINT, for testing purpose. For that you need to have password to create a key, which will be used to decrypt the `creds.py.enc` file.
       Once you decrypt your file, then you can use **through-python-sdk-for-cog.py** to run the code. 
       
       For this step you need password to generate a secret key, for that password, you can ping me on hangout.
       
## NOTE 
Don't upload your creds on github, always encrypt your creds before pushing your code. Use encrypt_file.py
