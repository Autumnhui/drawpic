# Author: Autumnhui
from PIL import Image, ImageDraw, ImageFont

font_size = 7   # 字体大小
text = "文字内容"   #文字内容
img_path = "/Users/autumnhui/Desktop/show.jpeg"  # 图片来源

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0,0,0)) # rgb色彩代码，默认覆盖为黑色
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('/Library/Fonts/STHeiti Medium.ttc', font_size) # 字体路径

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

img_new.convert('RGB').save("show1.jpeg") # 文件导出（可以增加路径）
