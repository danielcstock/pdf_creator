from PdfGenerator import PdfCanvas

pdf = PdfCanvas("TESTE_Laninha.pdf")
pdf.addImages(["img1.jpeg", "img2.jpeg"])
pdf.createFile()