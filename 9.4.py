from PIL import Image, ImageDraw, ImageFont
img = Image.open("cp.png")
layer = Image.new("RGBA", img.size, (0, 0, 0, 0)) #Создаю новый прозрачный слой такого же размера
pen = ImageDraw.Draw(layer) #Создаю рисовалку
pen.text(
    (33, 333),
    "WATERMARKA",
    fill = (255, 255, 255, 50),
    font = ImageFont.truetype("arial.ttf", 250)
)
gotovoe = Image.alpha_composite(img, layer)
gotovoe.save("cp_watermark.png")