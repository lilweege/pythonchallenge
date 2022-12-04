from PIL import Image
d="22"


im = Image.open(f"{d}/white.gif")
sx, sy = im.size
canv = Image.new("P", (800, 200), 255)
cx, cy = 100, 100
o = 0

for i in range(im.n_frames):
    im.seek(i)
    for y in range(98, 103):
        for x in range(98, 103):
            p = im.getpixel((x,y))
            if p != 0:
                dx, dy = x-100, y-100
                break
        else: continue
        break
    cx += dx
    cy += dy
    if dx == 0 and dy == 0:
        o += 100
    canv.putpixel((cx+o, cy), 0)

canv.show()
