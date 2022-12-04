from PIL import Image
from collections import deque

d="24"
im = Image.open(f"{d}/maze.png")
sx, sy = im.size
WHITE = (255,255,255,255)
start = (sx-2, 0)
end = (1, sy-1)
edge = [[None]*sx for _ in range(sy)]
q = deque([start])
while q:
    ux, uy = q.popleft()
    if (ux, uy) == end:
        break
    for vx, vy in (ux+1, uy), (ux-1, uy), (ux, uy+1), (ux, uy-1):
        if 0 <= vx < sx and 0 <= vy < sy:
            if edge[vy][vx] is None and im.getpixel((vx, vy)) != WHITE:
                edge[vy][vx] = (ux, uy)
                q.append((vx, vy))

l = []
x, y = end
while (x, y) != start:
    l.append(im.getpixel((x,y))[0])
    x, y = edge[y][x]

with open(f"{d}/path.zip", "wb") as f:
    f.write(bytes(reversed(l[1::2])))

