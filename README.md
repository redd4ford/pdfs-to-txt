# pdfs-to-txt
a simple script that recognizes text from pictures in a .pdf file and forms a .txt file.
# How to use
- clone this repository
- install  *[poppler](https://poppler.freedesktop.org)*. a [stable version](http://blog.alivate.com.au/poppler-windows/) for Windows
- install *[tesseract-ocr](https://github.com/tesseract-ocr/tesseract)*
- set variables in the script:
```
POPPLER_PATH: should be the path to \bin in the Poppler installation folder

pytesseract.pytesseract.tesseract_cmd: should be the path to tesseract.exe in the Tesseract-OCR installation folder

PROJECT_PATH: path to the project folder (or any other folder for generated .txts)

PDFS_SOURCE: path to the folder which contains .pdfs to be converted
```
- install *requirements.txt* and run the script
