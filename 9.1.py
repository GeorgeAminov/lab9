from PIL import Image
img = Image.open("cp.png")
print(f"Размер: {img.size}")
print(f"Формат: {img.format}")
print(f"Цветовая модель: {img.mode}")
img.show()

