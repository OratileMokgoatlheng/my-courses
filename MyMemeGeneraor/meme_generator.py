from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, font_path="arial.ttf", font_size=50):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img) 
    
    # Get image dimensions
    image_width, image_height = img.size

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Font not found. Using default font.")