from PIL import Image, ImageDraw
from utils import load_font, add_text

def generate_meme(image_path, top_text, bottom_text, font_path="arial.ttf", font_size=50):
    # Load image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Get image dimensions
    image_width, image_height = img.size

    # Load font
    font = load_font(font_path, font_size)

    # Calculate max width for text
    max_text_width = image_width * 0.8

    # Add top and bottom text to image
    add_text(draw, top_text, font, ((image_width - max_text_width) / 2, 10), max_text_width)
    add_text(draw, bottom_text, font, ((image_width - max_text_width) / 2, image_height - 60), max_text_width)

    # Save the meme
    img.save("generated_meme.jpg")
    print("Meme generated successfully!")

# Example usage
if __name__ == "__main__":
    image_path = "meme_template.jpg"  # Replace with your meme template image path
    top_text = "TOP TEXT"
    bottom_text = "BOTTOM TEXT"
    generate_meme(image_path, top_text, bottom_text)
