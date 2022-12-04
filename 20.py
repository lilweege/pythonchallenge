import requests

d="20"
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
'''
x = 30202
while True:
    headers = { "Range": f"bytes={x+1}-2123456789" }
    r = requests.get(url, headers=headers, auth=("butter", "fly"))
    print(r.content)
    print(r.headers)
    print(x)
    if not r.ok: break
    n = r.headers["Content-Range"].split('-')[-1].split('/')[0]
    x = int(n)

x = 2123456789
while True:
    headers = { "Range": f"bytes={x-1}-2123456789" }
    r = requests.get(url, headers=headers, auth=("butter", "fly"))
    print(r.content)
    print(r.headers)
    print(x)
    if not r.ok: break
    n = r.headers["Content-Range"].split()[-1].split('-')[0]
    x = int(n)
# password is nickname backwards
# redavni
'''

x = 1152983631
headers = { "Range": f"bytes={x}-2123456789" }
r = requests.get(url, headers=headers, auth=("butter", "fly"))
with open(f"{d}/invader.zip", "wb") as f:
    f.write(r.content)
