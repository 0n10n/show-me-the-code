import random
from PIL import Image, ImageDraw, ImageFont

orig_pic="icon.jpg"
new_pic="icon-new.jpg"

print(f"new pic: {new_pic} ")
# 打开图像文件
original_image = Image.open(orig_pic)

copied_image = original_image.copy()
draw = ImageDraw.Draw(copied_image)
# 还是自备一个字体文件保险点
font = ImageFont.truetype("../res/Carre-JWja.ttf", copied_image.height * 0.1)

# 要添加的数字
number = random.randint(1, 99)

# 获取数字的宽度和高度

text_width = font.getlength(str(number))

# 计算数字的位置（右上角）
x = copied_image.width - text_width - copied_image.width*0.05
y = copied_image.height * 0.05

# 在图像上叠加数字
draw.text((x, y), str(number), fill=(230, 0, 0), font=font)

# 保存修改后的图像
copied_image.save(new_pic)

# 显示图像
copied_image.show()

