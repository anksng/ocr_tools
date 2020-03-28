import PIL
import pytesseract
from PIL import Image
import jsonargparse

def ocr(path):
    """
    Returns text using OCR and prints in the console.
    Operations in development :
        * Read multiple files from a directory.
        * Write text to text file.
        * Find OCR tool for extracting with coordinates and use pagexml to write data in xml format
        * GUI or micro service
    :param path: path to the image
    :return: str, TExt found by OCR in the image
    """
    images = Image.open(path)
    img = images.rotate(-90)
    print(pytesseract.image_to_string(img))





if __name__ == '__main__':
    parser = jsonargparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path to dir where image is stored')
    # parse arguments and initialize precessing by calling run_anonymization(config)
    config = parser.parse_args()
    ocr(config.path)