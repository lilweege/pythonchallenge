
d="12"
n=5
with open(f"{d}/evil2.gfx", "rb") as f:
    b = f.read()
    for i in range(n):
        with open(f"{d}/part{i}.jpg", "wb") as im:
            im.write(b[i::n])
