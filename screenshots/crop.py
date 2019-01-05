from PIL import Image

img = Image.open("screenshot.png")

area = (60, 20, 930, 610)

crop = img.crop(area)

crop.show()

https://api.telegram.org/bot741491798:AAGAVtjhldPVKyjkPPN0qicXo3hYDfpjVFw/setWebhook?url=https://jazanu.000webhostapp.com/bd.php