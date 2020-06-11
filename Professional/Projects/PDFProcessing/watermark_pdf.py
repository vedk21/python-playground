# Watermarking all pdf pages

import PyPDF2

template = PyPDF2.PdfFileReader(open('resources/twopage.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('resources/wt.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

with open('resources/watermarked_twopage.pdf', 'wb') as file:
  output.write(file)
