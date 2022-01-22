from PIL import Image, ImageDraw
import random

# ベタ画像作成, 引数は(モード、サイズ、塗りつぶす色)
img = Image.new('RGBA', (500, 500))
draw = ImageDraw.Draw(img)

# 1ピクセルの点を描画
# draw.point((350, 200), fill=(255, 255, 0))

# 1点1点ランダムな色で描画
for i in range(500):
    for j in range(500):
        draw.point((i, j), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
img.save('draw.png', quality=95)

# ヒートマップのイメージ
img2 = Image.new('RGBA', (500, 500))
draw2 = ImageDraw.Draw(img2)
for i in range(100):
    for j in range(100):
        draw2.point((100+i, 100+j), fill=(255, 255, 200))
for i in range(100):
    for j in range(100):
        draw2.point((200+i, 100+j), fill=(255, 255, 0))
for i in range(100):
    for j in range(100):
        draw2.point((300+i, 100+j), fill=(255, 255, 200))
for i in range(100):
    for j in range(100):
        draw2.point((100+i, 200+j), fill=(255, 255, 0))
for i in range(100):
    for j in range(100):
        draw2.point((200+i, 200+j), fill=(255, 0, 0))
for i in range(100):
    for j in range(100):
        draw2.point((300+i, 200+j), fill=(255, 255, 0))
for i in range(100):
    for j in range(100):
        draw2.point((100+i, 300+j), fill=(255, 255, 200))
for i in range(100):
    for j in range(100):
        draw2.point((200+i, 300+j), fill=(255, 255, 0))
for i in range(100):
    for j in range(100):
        draw2.point((300+i, 300+j), fill=(255, 255, 200))
img2.save('draw2.png', quality=95)