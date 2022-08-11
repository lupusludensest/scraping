# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("E:/Gurov_SSD_256/My_docs/CV/CV_to_Vit_Krasnik_updated_with_Native_Digital.pdf")

# get number of pages
NumPages = object.getNumPages()
print(f'Total pages: "{NumPages}"')

# define keyterms
String = "Gurov"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    # print(f'This is page: "{str(i + 1)}"')
    Text = PageObj.extractText().replace(" ", "")
    ResSearch = re.search(String, Text)
    print(f'This is start of page "{str(i + 1)}" with text: "{Text}".\nThis is end of page "{str(i + 1)}". {String}: {ResSearch}\n{"*" * 120}')
