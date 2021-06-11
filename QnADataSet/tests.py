from django.test import TestCase
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import warnings
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your tests here.
def article():
    warnings.filterwarnings("ignore")
    nltk.download('punkt',quiet=True)
    article=Article('http://www.boun.edu.tr/tr-TR/Content/Ogrenciler/Ogrenci_Isleri/Sikca_sorulan_sorular')
    article.download()
    article.parse()
    article.nlp()
    takvim=article.text
    print(takvim)

def get_text():
    url = "https://www.hurriyet.com.tr/gundem/son-dakika-haberi-musilaj-sorunu-icin-kritik-gelisme-meclis-arastirma-komisyonu-kuruldu-41829652"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)

get_text()
#article()