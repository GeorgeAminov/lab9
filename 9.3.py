from PIL import Image, ImageFilter
for i in range(1,6):
    img = Image.open(f"{i}.jpg")
    img_filter = img.filter(ImageFilter.CONTOUR)
    img_filter.save(f"new/{i}_filter.jpg")