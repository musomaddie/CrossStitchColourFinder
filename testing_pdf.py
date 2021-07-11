import PyPDF2

pdfFileObj = open("pdfs/chart.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# print(pdfReader.numPages)

pageObj = pdfReader.getPage(pdfReader.numPages - 2)

print(pageObj.extractText())


pdfFileObj.close()
