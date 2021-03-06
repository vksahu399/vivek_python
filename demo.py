#!/usr/bin/env python
"Make some simple multipage pdf files."

from __future__ import print_function
from sys import argv

from reportlab.pdfgen import canvas

point = 1
inch = 72

TEXT = """%s    page %d of %d
Sample file created using python"""


def make_pdf_file(output_filename, np):
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    
    for pn in range(1, np + 1):
        v = 10 * inch
        for subtline in (TEXT % (output_filename, pn, np)).split( '\n' ):
            c.setStrokeColorRGB(0,0,10)
            c.setFillColorRGB(0,20,0)
            c.setFont("Helvetica", 12 * point)
            c.drawString( 1 * inch, v, subtline )
            v -= 12 * point
        c.showPage()
    c.save()

if __name__ == "__main__":
    nps = [None, 2, 2, 2]
    for i, np in enumerate(nps):
        if np:
            filename = "demosimple%d.pdf" % i
            make_pdf_file(filename, np)
            print ("Wrote", filename)