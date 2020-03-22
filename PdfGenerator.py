from reportlab.pdfgen import canvas

''' Class based on the reportlab.pdfgen's canvas.
'''
class PdfCanvas(object):
    def __init__(self, filename, pagesize=(595.27, 841.89), bottomup=1, pageCompression=0):
        self.canvas = canvas.Canvas(filename, pagesize, bottomup, pageCompression)

    ''' Hello world function.
    '''
    def hello(self):
        from reportlab.lib.units import inch
        # move the origin up and to the left
        self.setPagination()
        self.canvas.translate(inch,inch)
        # define a large font
        self.canvas.setFont("Helvetica", 14)
        # choose some colors
        self.canvas.setStrokeColorRGB(0.2,0.5,0.3)
        self.canvas.setFillColorRGB(1,0,1)
        # draw some lines
        self.canvas.line(0,0,0,1.7*inch)
        self.canvas.line(0,0,1*inch,0)
        # draw a rectangle
        self.canvas.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
        # make text go straight up
        self.canvas.rotate(90)
        # change color
        self.canvas.setFillColorRGB(0,0,0.77)
        # say hello (note after rotate the y coord needs to be negative!)
        self.canvas.drawString(0.3*inch, -inch, "Hello World")
        self.canvas.showPage()

    ''' Prints the page number. It gets the font parameters and the string position.
    '''
    def setPagination(self, fontStyle="Courier", fontSize=9, position="top", side="right"):
        self.canvas.setFont(fontStyle, fontSize)
        index = self.canvas.getPageNumber()
        x = 580 if side == "right" else 5
        y = 5 if position == "bottom" else 820
        self.canvas.drawString(x, y, "{}".format(index))

    ''' Adds one image per page.
    '''
    def addImages(self, images, pageSize = (595.27, 841.89)):
        width, height = pageSize
        for img in images:
            self.canvas.drawImage(img, 0, 0, width, height)
            self.setPagination(side="right", position="bottom")
            self.canvas.showPage()
    
    ''' Generate the pdf file on the current directory.
    '''
    def createFile(self):
        self.canvas.save()



