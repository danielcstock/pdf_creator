from reportlab.pdfgen import canvas

pdf = canvas.Canvas("TESTE_PDF.pdf")
pdf.drawString(100, 200, "exemplo de pdf.")
pdf.save()