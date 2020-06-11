# PDF processing

import PyPDF2
import sys

files = sys.argv[1:]

def pdf_merger(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(pdf)
  merger.write('resources/merged.pdf')

pdf_merger(files)
