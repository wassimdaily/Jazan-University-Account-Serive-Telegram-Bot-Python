from PIL import Image

img = Image.open("screenshot.png")

area = (60, 20, 930, 610)

crop = img.crop(area)

crop.show()
