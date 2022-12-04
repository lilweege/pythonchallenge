from difflib import Differ

d="18"
with open(f"{d}/deltas") as f:
    lines = f.readlines()

i1 = []
i2 = []
for line in lines:
    i1.append(' '.join(line[54:].strip().split()))
    i2.append(' '.join(line[:54].strip().split()))

both = open(f"{d}/both.jpg", "wb")
im1 = open(f"{d}/im1.jpg", "wb")
im2 = open(f"{d}/im2.jpg", "wb")

for x in Differ().compare(i1, i2):
    e = x[:1]
    l = bytes([int(c, 16) for c in x[2:].split()])
    if e == ' ': both.write(l)
    elif e == '+': im1.write(l)
    elif e == '-': im2.write(l)

both.close()
im1.close()
im2.close()
