import zipfile
d = "6"
z = zipfile.ZipFile(f"{d}/channel.zip")
z.extractall(d)

b = ""
x = 90052
while True:
    fn = f"{x}.txt"
    with open(f"{d}/{fn}") as f:
        s = f.read()
        # print(s)
        b += z.getinfo(fn).comment.decode()
        try:
            x = int(s.split()[-1])
        except: break
print(b)