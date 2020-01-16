from PIL import Image
im = Image.open("out copy.png")
pixels = im.load()

print (pixels[0, 0])