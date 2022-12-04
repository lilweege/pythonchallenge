from PIL import Image

d="16"
im = Image.open(f"{d}/mozart.gif")
sx, sy = im.size
p = 195
for y in range(sy):
    dim = (0,y,sx,y+1)
    row = im.crop(dim).tobytes()
    i = row.index(p)
    row = Image.frombytes(im.mode, (sx,1), row[i:]+row[:i])
    im.paste(row, dim)
im.show()
