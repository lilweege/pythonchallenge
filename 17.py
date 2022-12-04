import requests
'''
import bz2

from xmlrpc.client import ServerProxy

x = 12345
s = set()
l = []
while True:
    if x in s:
        print("LOOP")
        break
    s.add(x)
    r = requests.get(url=f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={x}")
    t = r.text
    c = r.cookies.get_dict()["info"]
    print(t, c)
    l.append(c)
    try:
        x = int(t.split()[-1])
    except ValueError:
        break

# python3 unquote is very different from python2
# this is suck
# s = unquote(''.join(l))
for i, c in enumerate(l):
    if len(c) > 1:
        l[i] = int(c[1:], 16)
    else:
        l[i] = ord(c)

print(bz2.decompress(bytes(l)))
# b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'

with ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as client:
    # call his father
    print(client.phone("Leopold"))
'''
# violin.php
msg = "the flowers are on their way"
print(requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php", cookies={"info": msg}).text)
