import easyocr
import cv2
image_path = r'C:\Users\sarda\OneDrive\Desktop\PythonCodes\PotfolioProjects\ImageRecogWebScrape\data\raw\images\Acetaminophen--L484--1.jpg'
def easy_ocr_image_to_text(image_path):
    # Create a reader object
    reader = easyocr.Reader(['en'])  # pass language code
    # Read the image
    image = cv2.imread(image_path)
    # Extract text from image
    result = reader.readtext(image)
    # Process result
    text = ' '.join([res[1] for res in result])
    return text

# Example usage
image_path = 'path_to_your_image.jpg'
text = easy_ocr_image_to_text(image_path)
print(text)
