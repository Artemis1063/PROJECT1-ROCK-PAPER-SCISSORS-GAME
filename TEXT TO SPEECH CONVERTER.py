#Import the libraries and they must be downloaded
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://www.abuad.edu.ng/')

article.download()
article.parse()


nltk.download('punkt')
article.nlp()

#Get the articles text
mytext = article.text

language = 'en' 

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("read_article.mp3")

os.system("start read_article.mp3")