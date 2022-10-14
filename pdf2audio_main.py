#First run 'pip install PyPDF2' & 'pip install pyttsx3' one by one in terminal of pycharm then execute the below program

import PyPDF2, pyttsx3
path = open('Example1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)
speak = pyttsx3.init()
for pages in range(pdfReader.numPages):
    text = pdfReader.getPage(pages).extractText()
    speak.say(text)
    speak.runAndWait()
speak.stop()