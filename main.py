from PdfGenerator import PdfCanvas

pdf = PdfCanvas("test.pdf")
pdf.addImages(["img1.jpeg", "img2.jpeg"])
pdf.createFile()