#############################
## 生成字母验证码图片
## 参考资料
## https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
## 

from PIL import Image, ImageDraw, ImageFont
import random
import string

# 生成随机字母
def generate_random_letters(length):
    return ''.join(random.choices(string.ascii_uppercase+string.digits, k=length))

# 创建验证码图片
def create_captcha_image(text, font_path, font_size, image_size):
    # 创建白色背景图片
    image = Image.new('RGB', image_size, color = 'white')
    
    # 在图片上绘制字母
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((10,10), text, font=font, fill='black')
    
    return image

# 生成随机字母
random_letters = generate_random_letters(4)

# 创建验证码图片
captcha_image = create_captcha_image(random_letters, "../res/Jersey10Charted-Regular.ttf", 48, (100, 60))

# 保存图片
captcha_image.save(f'captcha_image_{random_letters}.png')

# 显示图片（可选）
captcha_image.show()
