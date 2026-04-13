import pyttsx3
import PyPDF2
from tkinter.filedialog import *
import subprocess
import os

book=askopenfilename()
os.startfile(book)  

pdfreader=PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

player=pyttsx3.init()

for num in range(0, pages):
    page=pdfreader.pages[num]
    text=page.extract_text()
    player.say(text)
player.runAndWait()


