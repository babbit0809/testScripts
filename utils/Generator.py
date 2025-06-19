import os
from faker import Faker
from PIL import Image, ImageFont, ImageDraw
from config.PathConfig import Download_path

fake = Faker('zh_CN')


def random_str():
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)


def random_card_number():
    return fake.credit_card_number()


def pic_generator(width, height, file_name="test_pic", pic_format=".jpg", draw_text="test", text_size=20):
    image = Image.new("RGB", (width, height), color='black')
    font = ImageFont.truetype("arial.ttf", size=text_size)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(draw_text, font=font)
    draw.text(((width - w) / 2, (height - h) / 2), text=draw_text, fill='white', font=font)
    file_name = file_name + pic_format
    pic_path = os.path.join(Download_path, file_name)
    image.save(pic_path)
    return pic_path


if __name__ == '__main__':
    pass
