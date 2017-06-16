from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("D:/pics/fonts/arial.ttf", 50)
im = Image.open("D:/pics/20140824.jpeg")
w, h = im.size
draw = ImageDraw.Draw(im)
draw.text((w-40, 0), u'4', fill=(255, 0, 0), font=font)
im.save("D:/pics/20140824-1.jpeg")
