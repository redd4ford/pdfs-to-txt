from PIL import Image
import pytesseract
from time import time
from pdf2image import convert_from_path
import os

POPPLER_PATH = r'PATH_TO_POPPLER\BIN'
pytesseract.pytesseract.tesseract_cmd = r'PATH_TO_TESSERACT.EXE'
PROJECT_PATH = r'PATH_TO_PROJECT'
PDFS_SOURCE = r'PATH_TO_PDF_FILES'

pdf_filenames = [file for file in os.listdir(PDFS_SOURCE) if file.endswith('.pdf')]

print(f'FILES FOUND: {len(pdf_filenames)}')

if len(pdf_filenames) == 0:
    print('Nothing to convert. Please check your PDFS_SOURCE.')

else:
    start = time()
    merged_data = ''
    for file_pdf in pdf_filenames:
        # PDF -> image
        pages = convert_from_path(f'{PDFS_SOURCE}\\{file_pdf}', 500, poppler_path=POPPLER_PATH)

        for count, page in enumerate(pages):
            page.save(f'page_{count}.jpg', 'JPEG')

        # image -> text
        with open(f'{file_pdf[:-4]}.txt', 'a') as f:
            for i in range(len(pages)):
                # get text from image and avoid words being separated at line endings
                text = str((pytesseract.image_to_string(Image.open(f'page_{i}.jpg')))).replace('-\n', '')
                f.write(text)
                merged_data += text + '\n'

    for file_jpg in [file for file in os.listdir(PROJECT_PATH) if file.endswith('.jpg')]:
        path_to_jpg = os.path.join(PROJECT_PATH, file_jpg)
        os.remove(path_to_jpg)

    if len(pdf_filenames) > 1:
        answer = input('Would you like to merge all the .txts into one file? (y/n) ')
        if answer.startswith('y'):
            for file_txt in [file for file in os.listdir(PROJECT_PATH) if file.endswith('.txt')]:
                path_to_txt = os.path.join(PROJECT_PATH, file_txt)
                os.remove(path_to_txt)
            with open('merged.txt', 'a') as f:
                f.write(merged_data)
    merged_data = ''

    print(f'ELAPSED TIME: {time() - start}')
