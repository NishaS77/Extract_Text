# extract text from an image
from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image_path = r'download.png'

# open Image
img = Image.open(image_path)

# location of tesseract library
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img)
print(text)