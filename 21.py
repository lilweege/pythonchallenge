import zlib
import bz2
d="21"

with open(f"{d}/package.pack", "rb") as f:
    d = f.read()

while True:
    c = chr(d[0])
    b = chr(d[-1])
    if c == 'B': # bzip2
        d = bz2.decompress(d)
        print("B", end="")
    elif c == 'x': # zlib
        d = zlib.decompress(d)
        print("z", end="")
    elif b == 'B' or b == 'x':
        d = d[::-1]
        print()
    else:
        break
print()
print(d)
