#pyttsx - python text to speech
import pyttsx3
'''pypdf2 - perform different operations on pdf such as
read,write and merge pdf.'''
import PyPDF2

book = open('dummy1.pdf', 'rb')

#pdffilereader - perform operations related to reading
pdfreader = PyPDF2.PdfFileReader(book)

#numpages - count number of pages
pages = pdfreader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfreader.getPage(0)
text = page.extractText()
speaker.say(text)

#makes speech audible in system
speaker.runAndWait()