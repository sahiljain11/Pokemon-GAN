from PIL import Image
import numpy as np

def change_resolution(img,newsize):
	#change img resolution to newsize x newsize
	return img.resize((newsize,newsize))

img = Image.open('platinum/1.png')
for i in range(50,51):
	new_img = change_resolution(change_resolution(img,i),80)

new_img.save("snewimg.png", "PNG", optimize=True)