# Image module can help interact with image
# ImageOps contain function can process the image 
from PIL import Image, ImageOps

def invert_grayscale(image_path, save_path):
        img = Image.open(image_path).convert("L")  # Grayscale
        inverted = ImageOps.invert(img)
        inverted.save(save_path)
        inverted.show()

invert_grayscale("smokey.jpg", "smokey_bw_inverted.jpg")
