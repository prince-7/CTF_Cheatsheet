from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
im = Image.open("out copy.jpg")
pixels = im.load()
pixels = list(im.getdata())
new_pixel=[[0]*304]*92
for i in range (0,92):
	new_pixel[i]=[pixels[i+92*j] for j in range(0,304)]
print (new_pixel)
plt.savefig("out.jpg")


