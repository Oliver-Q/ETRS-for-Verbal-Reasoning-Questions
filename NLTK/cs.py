#coding:utf8

import time

import pandas as pd

import string

def load_words(dic_file='./Freq/SogouLabDic.dic'):

    t=time.time()

    word_dic={}

    first_word_dic={}

    for line in open(dic_file):

        line=unicode(line,'utf8').split()

        word=line[0]

        word_len=line[1]

        sex=line[2] if len(line)==3 else None

        first_word_dic.setdefault(word[0],[])

        first_word_dic[word[0]].append(word)

        word_dic[word]=(word_len,sex)

    for first_word,words in first_word_dic.items():

        word_dic[first_word]=sorted(words,key=lambda x:len(x),reverse=False)

    print 'load_words time:',time.time()-t

    return first_word_dic,word_dic

first_word_dic,word_dic=load_words()

model_dic={

    'letters':string.ascii_letters,

    'digits':string.digits,

    'punctuation':string.punctuation,

    }

def match_ascii(i,sentence):

    result=''

    for i in range(i,len(sentence)):

        if not sentence[i] in string.ascii_letters:break

        result +=sentence[i]

    return result

def match_word(i,sentence,first_word_dic=first_word_dic):

    first_word=sentence[i]

    if not first_word_dic.has_key(first_word):

        if first_word in string.ascii_letters:

            return match_ascii(i,sentence)

        return ' '

    words=first_word_dic[first_word]

    for word in words:

        if sentence[i:i+len(word)]==word:

            return word

    return first_word

def perse(sentence):

    if sentence:

        words=[]

        i=0

        while i <len(sentence):

            matched_word=match_word(i,sentence)

            if not matched_word==' ':words.append(matched_word)

            i +=len(matched_word)

        return words

if __name__=='__main__':

    sentence=u'我曾经跨过山和abd dfdf大海!互,联网词语搭配关系库来自于对SOGOU搜索引擎所索引到的中文互联网语料的统计分析，统计所进行的时间是2006年10月，涉及到的互联网语料规模在1亿页面以上。涉及到的搭配样例超过2000万，涉及到的高频词超过15万。'

    words=perse(sentence)

    for w in words :print w