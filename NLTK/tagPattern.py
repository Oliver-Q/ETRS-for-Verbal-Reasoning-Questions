# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:06:19 2017

@author: Q-PC
"""

import nltk
text = nltk.word_tokenize("It is refreshing to read a book about our planet by an author who does not allow \
facts to be __________ by politics: well aware of the political disputes about \
the effects of human activities on climate and biodiversity, this author does not \
permit them to __________ his comprehensive description of what we know \
about our biosphere. He emphasizes the enormous gaps in our knowledge, the \
sparseness of our observations, and the __________, calling attention to the \
many aspects of planetary evolution that must be better understood before we \
can accurately diagnose the condition of our planet.")

# print nltk.pos_tag(text)

from nltk.tag import RegexpTagger
# define regex tag patterns
patterns = [
        (r'.*who$', 'Clause'),  
        (r'.*what$', 'Clause'),  
        (r'.*It$', 'Clause'),          #
        (r'.*:$', 'Repeat'),                # simple past
        (r'.*not$', 'Reverse'),                # 3rd singular present
        (r'.*this$', 'Refer'),     
        (r'.*them$', 'Refer'),         
        (r'.*better$', 'Positive'),  
        (r'.*dispute$', 'Negative'), 
        (r'.*', 'NN')                     # nouns (default) ... 
]
rt = RegexpTagger(patterns)

print rt.tag(text)
