from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, font_path="arial.ttf", font_size=50):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)