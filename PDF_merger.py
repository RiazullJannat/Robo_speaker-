import PyPDF2
def pdf_merger(files):
    merger = PyPDF2.PdfFileMerger()
    for file in files:
        pdffile = open(file,'rb')
        pdfread = PyPDF2.PdfFileReader(pdffile,strict=False)
        merger.append(pdfread)
        pdffile.close()
    merger.write("New_Merged_file.pdf")

file = ['1.pdf','2.pdf','3.pdf']
pdf_merger(file)
