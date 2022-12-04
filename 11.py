from PIL import Image

d="11"
im = Image.open(f"{d}/cave.jpg")
sx, sy = im.size
small = im.resize((sx//2, sy//2), Image.NEAREST)
small.show()
