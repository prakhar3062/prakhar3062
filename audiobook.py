import pyttsx3
import PyPDF2
book=open('mathb.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()

page=pdfReader.getPage(496)
text=page.extractText()
speaker.say(text)
speaker.say('done')
speaker.runAndWait()
