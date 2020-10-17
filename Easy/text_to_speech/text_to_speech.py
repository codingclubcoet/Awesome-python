#this program can be used to convert pdf text documents to speech using text to speech module.

import pyttsx3
import PyPDF2
book = open('spectre.pdf', 'rb') 
#replace filename.pdf with the name of your pdf file

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
        text = page.extractText()
            speaker.say(text)
                speaker.runAndWait()
