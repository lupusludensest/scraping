from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open("E:\Gurov_SSD_256\My_docs\CV\Deloitte_dt_28_April_2021\Viacheslav_Gurov_EH_Offer_Deloitte_dt_28_apr_2021.pdf", 'rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()