from PIL import Image

d="7"
i = Image.open(f"{d}/oxygen.png")
strip = i.crop((0,49,608,50))

# scl=7
# for x in range((strip.width+1)//scl):
#     print(chr(strip.getpixel((x*scl,0))[0]), end="")

l=[105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(x) for x in l))