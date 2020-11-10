from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys, fitz
import os


img = Image.open(r"C:\Users\usuario\Desktop\valeasprog\generico.png")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype(r"arial.ttf", 122)

pdf = str ('.pdf')
png = str('.png')
x = input("nombre de la caratula:  ")
# draw.text((x, y),"soy el mejor programador del universo",(r,g,b))
name = draw.text((655, 2801), x ,(0,0,0),font=font)
 



img.save(r'C:\Users\usuario\Desktop\CARATULA\ '+x+png)
print("se ha creado correctamente la caratula de: " +x)


print("Convirtiendo en pdf...")

imglist=[r'C:\Users\usuario\Desktop\CARATULA\ '+x+png]

doc = fitz.open()                            # PDF with the pictures
for i, f in enumerate(imglist):
    img = fitz.open(f) # open pic as document
    rect = img[0].rect                       # pic dimension
    pdfbytes = img.convertToPDF()            # make a PDF stream
    img.close()                              # no longer needed
    imgPDF = fitz.open("pdf", pdfbytes)      # open stream as PDF
    page = doc.newPage(width = rect.width,   # new page with ...
                       height = rect.height) # pic dimension
    page.showPDFpage(rect, imgPDF, 0) 
           # image fills the page
doc.save(r'C:\Users\usuario\Desktop\CARATULA\ '+x+pdf)

print("Convertido a PDF y guardado correctamente")