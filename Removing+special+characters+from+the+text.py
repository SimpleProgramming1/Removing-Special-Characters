


# Creating Beautiful Soup object

from bs4 import BeautifulSoup
import urllib.request

page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')

soup=BeautifulSoup(page,'html.parser')


print(soup)


# Word count frequency calculation

import nltk
from nltk.tokenize import word_tokenize




text=soup.get_text(strip=True)

print(text)



word_tokens=word_tokenize(text)

print(word_tokens)


cts=nltk.FreqDist(word_tokens)

cts.plot(20)


# Removing special characters


import re


text2= re.sub("[^A-Za-z]+"," ",text)
print(text2)




# Word count frequency calculation for modified dataset

import nltk
from nltk.tokenize import word_tokenize



word_tokens=word_tokenize(text2)

print(word_tokens)


cts=nltk.FreqDist(word_tokens)

cts.plot(20)






