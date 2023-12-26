from PIL import Image
import pytesseract
import os
import config
import clipboard

pytesseract.pytesseract.tesseract_cmd = fr'{config.TESSERACT_PATH}'


class ExtractTheTextFromImage():
    def __init__(self, image):
        self.image_path = image

    def loadTheImageProcessIt(self):
        result = self.extract_kannada_text(self.image_path)
        return result

    def extract_kannada_text(self, image_path):
        # Open the image using Pillow
        img = Image.open(image_path)

        # Use Tesseract to extract text
        text = pytesseract.image_to_string(img, lang='kan')

        return text
    
def processTheImage(image=config.SAVE_IMAGE_PATH):
    piet = ExtractTheTextFromImage(image)
    text = piet.loadTheImageProcessIt()
    clipboard.copy(text)

