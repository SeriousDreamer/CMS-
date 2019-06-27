from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from cms.settings import BASE_DIR
import os
import io

CHECK_CODE = ''


# 随机字母:
def rndChar():
    single_char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    nun = random.randint(0, 58)
    global CHECK_CODE
    CHECK_CODE += single_char[nun]
    return single_char[nun]


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def create_code():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('simheittf.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(255, 255, 255))
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 画出线
    for i in range(4):
        draw.line((random.randint(0, 240), random.randint(0, 60), random.randint(0, 240), random.randint(0, 60)),
                  'cyan')
    # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    # image.save(os.path.join(BASE_DIR, 'static/images/checkCode/code.png'), 'png')
    buf = io.BytesIO()
    image.save(buf,'png')
    global CHECK_CODE
    result = CHECK_CODE
    CHECK_CODE = ""
    return result, buf

# create_code()
