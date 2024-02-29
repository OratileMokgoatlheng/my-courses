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


        # Calculate text size and position
    text_width, text_height = draw.textsize(top_text, font=font)
    x_top = (image_width - text_width) / 2
    y_top = 10

    text_width, text_height = draw.textsize(bottom_text, font=font)
    x_bottom = (image_width - text_width) / 2
    y_bottom = image_height - text_height - 10

     # Add text to image
    draw.text((x_top, y_top), top_text, fill="white", font=font, stroke_width=2, stroke_fill="black")
    draw.text((x_bottom, y_bottom), bottom_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

    # Save the meme
    img.save("generated_meme.jpg")
    print("Meme generated successfully!")

# Example usage
image_path = "meme_template.jpg"  # Replace with your meme template image path
top_text = "TOP TEXT"
bottom_text = "BOTTOM TEXT"
generate_meme(image_path, top_text, bottom_text)