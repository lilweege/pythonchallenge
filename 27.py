from PIL import Image

d="27"
i = Image.open(f"{d}/zigzag.gif")
print(i.getpalette())