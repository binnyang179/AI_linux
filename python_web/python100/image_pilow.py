from PIL import Image

image = Image.open('daijia.jpg')

print(image.format)
print(image.size)
print(image.mode)
image.show()


image = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
image.crop(rect).show()

image = Image.open('./res/guido.jpg')
size = 128, 128
image.thumbnail(size)
image.show()


image1 = Image.open('./res/luohao.png')
image2 = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))


image = Image.open('./res/guido.png')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()


image = Image.open('./res/guido.jpg')
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

image.show()


from PIL import Image, ImageFilter

image = Image.open('./res/guido.jpg')
image.filter(ImageFilter.CONTOUR).show()



