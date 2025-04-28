from pypdf import PdfReader
from gtts import gTTS
import os



# creating a pdf reader object
reader = PdfReader('somepdffile.pdf')

# making sentence variable
sentence=[]


# looping through pages to read all pdf file
for i in range(len(reader.pages)):
    page = reader.pages[i]
    sentence.append(page.extract_text())

# cleaning appended text
txt = ' '.join(sentence)


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
obj = gTTS(text=txt, lang=language, slow=False)

# Saving the converted audio in a mp3 file named.
# welcome
obj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")