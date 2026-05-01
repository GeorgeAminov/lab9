from PIL import Image, ImageOps
img = Image.open("cp.png")
i, j = img.size
k = (i // 3, j // 3)
small_img = img.resize(k)
small_img.save("small_cp.png")
mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img.save("mirror_cp.png")
flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
flip_img.save("flip_cp.png")
#mirror_img = ImageOps.mirror(img)
#mirror_img.save("mirror_cp.png")
#flip_img = ImageOps.flip(img)
#flip_img.save("flip_cp.png")