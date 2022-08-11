# Import the libraries
import os
import pandas as pd
import numpy as np
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

# Assign the variables
sourceLoc = "E:/Gurov_SSD_256/My_docs/CV/Deloitte_dt_28_April_2021/"
outLoc = "E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\scraping"
searchString = "deloitte"
fileType = ".pdf"

direc = os.listdir(sourceLoc)
direc

fileList = []
# For loop to search for the string
for file in direc:
    if file.endswith(fileType):
        f = open(sourceLoc + file, 'r')
        if searchString in f.read():
            fileList.append(file)
        f.close()
print(fileList)

# DataFrame creation and export to excel
file_with_word_is_found = pd.DataFrame(fileList, columns=['FileName'], index=range(0, len(fileList)))
file_with_word_is_found.to_excel(outLoc + "file_with_word_is_found.xlsx", index=False)