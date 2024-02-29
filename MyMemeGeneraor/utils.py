from PIL import ImageFont, ImageDraw

def load_font(font_path, font_size):
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Font not found. Using default font.")
    return font