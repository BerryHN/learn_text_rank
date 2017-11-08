# -*- coding: utf-8 -*-
# author:BerryHN
from nltk.tokenize import sent_tokenize,word_tokenize

from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

file=open('news.txt','r')
text=file.read().replace('\n','')


sents=sent_tokenize(text)

word_sent=[word_tokenize(s.lower()) for s in sents]

print word_sent