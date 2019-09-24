from PIL import Image

def change_resolution(img,newsize):
	#change img resolution to newsize x newsize
	return img.resize((newsize,newsize))

img = Image.open('platinum/1.png')
for i in range(4,80):
	new_img = change_resolution(img)

# new_img.save("newimg.png", "PNG", optimize=True)