from PIL import Image, ImageDraw, ImageFont

# 打开图像文件
image = Image.open("input_image.jpg")

# 在图像上创建一个Draw对象
draw = ImageDraw.Draw(image)

# 设置字体
font = ImageFont.truetype("arial.ttf", 30)

# 要添加的数字
number = 1

# 获取数字的宽度和高度
text_width, text_height = draw.textsize(str(number), font=font)

# 计算数字的位置（右上角）
x = image.width - text_width - 10
y = 10

# 在图像上叠加数字
draw.text((x, y), str(number), fill=(255, 255, 255), font=font)

# 保存修改后的图像
image.save("output_image.jpg")

# 显示图像
image.show()

