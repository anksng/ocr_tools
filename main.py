import PIL
import pytesseract
import os
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
    :return: str, Text found by OCR in the image
    """
    # paths = glob.glob(path)
    # for i in paths:
    images = Image.open(path)
    # add pre processing here. Find pre processing discrepencies for various document types.
    img = images.rotate(-90)

    # write to text file
    with open(path.split('/')[-1].split('.')[0] + '.txt', 'w') as f:
        f.write(pytesseract.image_to_string(img))

    print(pytesseract.image_to_string(img))
    print('Text output in file -', 'ocr_tools/', path.split('/')[-1].split('.')[0] + '.txt')





if __name__ == '__main__':
    parser = jsonargparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path to dir where image is stored')
    # parse arguments and initialize precessing by calling run_anonymization(config)
    config = parser.parse_args()
    ocr(config.path)
