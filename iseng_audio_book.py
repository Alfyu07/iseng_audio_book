import pyttsx3
import PyPDF2

#buka pdf dan baca dengan binary mode
book = open('Buku Gratis - Mereka yang Merugi - Muhammad Abduh Tuasikal.pdf', 'rb')

#pakai PyPDF2 untuk baca buku
pdfReader = PyPDF2.PdfFileReader(book)

#lihat banyak pages
pages = pdfReader.numPages

#inisialisasi engine speaker dari pytssx3
speaker = pyttsx3.init()
#ambil property voices untuk melihat mode dan bahasa 
voices = speaker.getProperty('voices')

"""
property engine tssx bisa di atur dengan parameter2 dibawah ini
for index, voice in enumerate(voices):
    print("====" + str(index) + "====")
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
"""

#merubah voice yang digunakan ke bahasa indonesia
speaker.setProperty('voice', voices[34].id)

#definisiin variable start sebagai halaman awal
start= 12

for num in range(start, pages):
  page = pdfReader.getPage(num)
  text = page.extractText()
  print(text)
  speaker.say(text)
  speaker.runAndWait()
  
  
#resource : https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3#:~:text=For%20Windows%20user%2C%20head%20over,see%20the%20following%20user%20interface.&text=Apart%20from%20the%20default%20language,to%20add%20a%20preferred%20language.
