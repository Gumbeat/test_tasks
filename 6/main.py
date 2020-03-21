from PIL import Image, ImageDraw
from random import randint

width = 1000
height = 600

x = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y = []

for i in range(0, len(x), 2):
    y.append(600)
    y.append(randint(0, 300))


im = Image.new('RGB', (width, height), 'white')

draw = ImageDraw.Draw(im)


for i in range(0, len(x) - 2, 2):
    draw.polygon([(x[i], y[i]), (x[i + 1], y[i + 1]), (x[i + 2], y[i + 2])], fill='orangered')
    temp_y_1 = y[i + 1] + 200
    draw.polygon([(x[i] + 15, y[i]), (x[i + 1], temp_y_1), (x[i + 2] - 15, y[i + 2])], fill='coral')
    temp_y_2 = temp_y_1 + (600 - temp_y_1) / 2
    draw.polygon([(x[i] + 30, y[i]), (x[i + 1], temp_y_2), (x[i + 2] - 30, y[i + 2])], fill='gold')


im.show()

im.save('fire.png')
