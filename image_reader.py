from PIL import Image

img = Image.open('platinum/1.png')
for i in range(4,80):
	new_img = img.resize((i,i))

# new_img.save("newimg.png", "PNG", optimize=True)