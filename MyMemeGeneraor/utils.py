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

     Check if text exceeds max width
    if text_width > max_width:
        # If text exceeds max width, wrap it
        lines = []
        line = ''
        for word in text.split():
            if draw.textsize(line + word, font=font)[0] <= max_width:
                line += word + ' '
            else:
                lines.append(line)
                line = word + ' '
        lines.append(line)

        # Draw wrapped text
        y = position[1]
        for line in lines:
            draw.text((position[0], y), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
            y += text_height
    else:
        # If text fits within max width, draw normally
        draw.text(position, text, font=font, fill="white", stroke_width=2, stroke_fill="black")
