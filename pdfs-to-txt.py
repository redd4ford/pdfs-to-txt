from PIL import Image
import pytesseract
from time import time
from pdf2image import convert_from_path
import os

POPPLER_PATH = r'PATH_TO_POPPLER\BIN'
pytesseract.pytesseract.tesseract_cmd = r'PATH_TO_TESSERACT.EXE'
PROJECT_PATH = r'PATH_TO_PROJECT'
PDFS_SOURCE = r'PATH_TO_PDF_FILES'

start = time()
print(f'FILES FOUND: {len(os.listdir(PDFS_SOURCE))}')

for filename in os.listdir(PDFS_SOURCE):
    # PDF -> image
    pages = convert_from_path(f'{PDFS_SOURCE}\\{filename}', 500, poppler_path=POPPLER_PATH)

    for count, page in enumerate(pages):
        page.save(f'page_{count}.jpg', 'JPEG')

    # image -> text
    with open(f'{filename[:-4]}.txt', 'a') as f:
        for i in range(1, len(pages)):
            # get text from image and avoid words being separated at line endings
            text = str((pytesseract.image_to_string(Image.open(f'page_{i}.jpg')))).replace('-\n', '')
            f.write(text)

for file in [file for file in os.listdir(PROJECT_PATH) if file.endswith('.jpg')]:
    path_to_file = os.path.join(PROJECT_PATH, file)
    os.remove(path_to_file)

print(f'ELAPSED TIME: {time() - start}')
