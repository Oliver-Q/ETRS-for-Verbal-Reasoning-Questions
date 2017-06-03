# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.corpus import wordnet

# print wordnet.synsets('dog')

# dog = wordnet.synset('dog.n.01')
# print dog.definition()
# cat = wordnet.synset('cat.n.01')
# print dog.path_similarity(cat)

print wordnet.synsets('obscure')
obscure =  wordnet.synset('obscure.v.01')
print obscure.definition()