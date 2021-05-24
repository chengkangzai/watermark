from PIL import Image, ImageFont, ImageDraw
import os

# Change to your location
font = ImageFont.truetype('OpenSans-SemiboldItalic.ttf', 60)


# https://stackoverflow.com/a/1970930/12875691
# https://towardsdatascience.com/adding-text-on-image-using-python-2f5bf61bf448
def addText(imageSrc: str, prefix: str, number: int):
    ext = os.path.splitext(imageSrc)[1]

    image = Image.open(imageSrc)
    editableImage = ImageDraw.Draw(image)

    width, height = image.size
    draw = ImageDraw.Draw(image)

    text = f"""Pang Lai Enterprise \n {prefix}{number}"""

    w, h = draw.textsize(text, font=font)
    x = ((width - w) / 2)
    y = ((height - h) / 2) * 1.3
    editableImage.text((x, y), text, (255, 255, 255), font=font, align="center")

    image.save("[DONE] " + prefix + str(number) + ext)


files = [f for f in os.listdir('.') if os.path.isfile(f)]
prefix = input("What is the prefix").upper()
number = int(input("What is the starting number").replace(" ", ""))
for f in files:
    if (".jpg" in f or ".jpeg" in f or ".png" in f) and "[DONE]" not in f:
        addText(f, prefix, number)
        number = number + 1
