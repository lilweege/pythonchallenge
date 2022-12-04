from PIL import Image

d="14"
i = Image.open(f"{d}/wire.png")
j = Image.new("RGB", (100, 100))

# n=0
# for x in range(100):
#     for y in range(100):
#         j.putpixel((y,x), i.getpixel((n, 0)))
#         n += 1
# j.show()

walk = [99,100]
step = [(-1,0), (0,1), (1,0), (0,-1)]
x, y = 0, -1
n = 0
r = 1
while walk[r%2]:
    for _ in range(walk[r%2]):
        x += step[r][0]
        y += step[r][1]
        j.putpixel((y,x), i.getpixel((n,0)))
        n += 1
    walk[r%2] -= 1
    r = (r+1) % 4

j.show()
