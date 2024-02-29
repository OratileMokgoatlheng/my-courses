from PIL import ImageFont, ImageDraw

def load_font(font_path, font_size):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Font not found. Using default font.")
    return font

def add_text(draw, text, font, position, max_width):
    # Calculate text dimensions
    text_width, text_height = draw.textsize(text, font=font)