import pyttsx3
import PyPDF2

book = open('Buku Gratis - Mereka yang Merugi - Muhammad Abduh Tuasikal.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[34].id)

for num in range(12, pages):
  page = pdfReader.getPage(num)
  text = page.extractText()
  print(text)
  speaker.say(text)
  speaker.runAndWait()