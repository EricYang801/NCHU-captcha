from PIL import Image, ImageDraw, ImageFont
import random

def create_code(length=4):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(code_chars) for _ in range(length))

def draw_lines(draw, width, height, num_lines=70):
    for _ in range(num_lines):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill='grey', width=1)

def generate_code_image():
    img_width = 100
    img_height = 30
    background_color = '#8dd5e7'
    text_color = '#fff'
    font_size = 20

    # Create a new image with white background
    image = Image.new('RGB', (img_width, img_height), background_color)
    draw = ImageDraw.Draw(image)

    # Draw interference lines
    draw_lines(draw, img_width, img_height)

    # Choose a font
    font_path = "arial.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # Generate and draw the code
    code = create_code()
    draw.text((16, 5), code, fill=text_color, font=font)

    return image, code

if __name__ == "__main__":
    code_image, code = generate_code_image()
    code_image.show()  # 顯示圖片
    code_image.save("code_image.png")  # 儲存圖片
    print("Generated code:", code)
