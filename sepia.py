from PIL import Image

def sepia(image_path):
    # convert the image to grayscale then convert to RGB mode this is how to create black-white background before change to sepia effect
    img = Image.open(image_path).convert("L").convert("RGB")
    # Take all pixels of the image
    pixels = img.load()
    #Scan for all pixel from left to right, top to bottom
    for x in range(img.width):
        for y in range(img.height):
            # take the color value of the pixels at position(x, y)
            r, g, b = pixels[x, y]

            if r < 63:
                r, b = int(r * 1.1), int(b * 0.9)
            elif r < 192:
                r, b = int(r * 1.15), int(b * 0.85)
            else:
                r, b = min(int(r * 1.08), 255), int(b * 0.93)
            # Return the value by a tuple
            pixels[x, y] = (r, g, b)

    return img

# Test
output = sepia("smokey.jpg")
output.show()
