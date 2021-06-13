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


print("1. Set number randomly")
print("2. Set number by File Name")
operation = input("What's the operation :")
try:
    ope = int(operation)
    if ope <= 0 or ope >= 3:
        print("Invalid operation")
        exit()

    if ope == 1:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        prefix = input("What is the prefix :").upper()
        number = int(input("What is the starting number :").replace(" ", ""))
        print("PROCESSING...")
        for f in files:
            if (".jpg" in f or ".jpeg" in f or ".png" in f) and "[DONE]" not in f:
                addText(f, prefix, number)
                number = number + 1

    if ope == 2:
        print("WARNING : Pleas make sure the file have number in it")
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        prefix = input("What is the prefix : ").upper()
        print("PROCESSING...")
        for f in files:
            if (".jpg" in f or ".jpeg" in f or ".png" in f) and "[DONE]" not in f:
                number = int(f.replace(" ", "").split(".")[0])
                addText(f, prefix, number)

except ValueError:
    print("Input must be Number")
