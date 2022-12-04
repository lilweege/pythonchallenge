import requests

# x = 12345
x = 16044 // 2
s = set()
while True:
    if x in s:
        print("LOOP")
        break
    s.add(x)
    t = requests.get(url=f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={x}").text
    print(t)
    try:
        x = int(t.split()[-1])
    except: break