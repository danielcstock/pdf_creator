from PdfGenerator import PdfCanvas

pdf = PdfCanvas("test.pdf")
pdf.addImages(["assets/img1.jpeg", "assets/img2.jpeg", "assets/img3.jpeg"])
pdf.createFile()