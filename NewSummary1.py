# -*- coding: utf-8 -*-
# author:BerryHN
# -*- coding: utf-8 -*-
# author:BerryHN

import nltk

from nltk.tokenize  import sent_tokenize,word_tokenize
from nltk.corpus  import stopwords
from collections import defaultdict
from string import punctuation
from heapq  import nlargest


stopwords=set(stopwords.words('english')+list(punctuation))

max_cut=0.9
min_cut=0.1

"""

计算出每个次的频率
word_set  是一个已经分好词的列表
返回一个词典freq[]
freq【w】 代表次出现的频率

"""


def compute_frequencies(word_set):
    freq=defaultdict(int)
    for s in word_set:
        for word in s:
            if word not in stopwords:
                freq[word]+=1
    m=float(max(freq.values()))
    for w in list(freq.values()):
        freq[w]=freq[w]/m
        if freq[w]>=max_cut or freq[w]<=min_cut:
            del freq[w]

    return freq


def summarize(text,n):
    sents=sent_tokenize(text)
    assert  n<=len(sents)
    word_sent=[word_tokenize(s.lower()) for s in sents]
    freq=compute_frequencies(word_sent)
    ranking=defaultdict(int)
    for i ,word in enumerate(word_sent):
        for w in word:
            if w in freq:
                ranking[i]+=freq[w]
    sents_idex=rank(ranking,n)
    return [sents[j] for j in sents_idex]


def rank(ranking,n):
    return nlargest(n,ranking,key=ranking.get)


if __name__=='__main__':
    with open('news.txt','r') as myfile:
        text=myfile.read().replace('\n','')
    res=summarize(text,2)
    for i in range(len(res)):
        print(res[i])



