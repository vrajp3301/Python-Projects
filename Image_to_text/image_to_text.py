import pytesseract
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img=Image.open('1.jpg')
text=pytesseract.image_to_string(img)
file = open(r"C:\Users\ADMIN\Desktop\Python\another.txt","a")
file.writelines(text)
file.close()
