import cv2
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r'C:\Users\sarda\OneDrive\Desktop\PythonCodes\PotfolioProjects\ImageRecogWebScrape\data\raw\images\Atorvastatin Calcium--APO ATV20--1.jpg'
image = cv2.imread(image_path)

# Check if the image is read correctly
if image is None:
    print("The image could not be read. Please check the file path.")
else:

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 90, 215, cv2.THRESH_BINARY)
    inverted_image = cv2.bitwise_not(binary_image)
    text = pytesseract.image_to_string(inverted_image)
    print("Detected text:", text)
    #show image static
    cv2.imshow("Image", inverted_image)
    cv2.waitKey(0)