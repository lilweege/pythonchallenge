# I had to look this up cause I didn't get an email back -_-
'''
From: leopold.moz@pythonchallenge.com Subject: Re: sorry Date:
Never mind that.
Have you found my broken zip?
md5: bbb8b499a0eef99b52c7f13f4e78c24b
Can you believe what one mistake can lead to?
'''

import hashlib
# this challenge kinda sucked cause I could already unzip and preview the image despite one single corrupt byte
# the hardest part was figuring out that "speedboat" was the next word, like I guessed "speed" 100 times already

d="26"
with open(f"{d}/mybroken.zip", "rb") as f:
    x = f.read()

md5 = "bbb8b499a0eef99b52c7f13f4e78c24b"
n = len(x)
x = list(x)
for i, b in enumerate(x):
    for nb in range(256):
        x[i] = nb
        if hashlib.md5(bytes(x)).hexdigest() == md5:
            with open(f"{d}/fixed.zip", "wb") as f:
                f.write(bytes(x))
            exit(0)
    x[i] = b
