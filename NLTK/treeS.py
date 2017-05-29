# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:23:48 2017

@author: Q-PC
"""


from pattern.en import parsetree, Chunk
from nltk.tree import Tree

sentence = "In parts of the Arctic, the land grades into the landfast ice so _\
 that you can walk off the coast and not know you are over the hidden sea."

tree = parsetree(sentence)

for sentence_tree in tree:
    print sentence_tree.chunks
    
for sentence_tree in tree:
    for chunk in sentence_tree.chunks:
        print chunk.type, '->', [(word.string, word.type) 
                                 for word in chunk.words]
        

def create_sentence_tree(sentence, lemmatize=False):
    sentence_tree = parsetree(sentence, 
                              relations=True, 
                              lemmata=lemmatize)
    return sentence_tree[0]
    
def get_sentence_tree_constituents(sentence_tree):
    return sentence_tree.constituents()
    
def process_sentence_tree(sentence_tree):
    
    tree_constituents = get_sentence_tree_constituents(sentence_tree)
    processed_tree = [
                        (item.type,
                         [
                             (w.string, w.type)
                             for w in item.words
                         ]
                        )
                        if type(item) == Chunk
                        else ('-',
                              [
                                   (item.string, item.type)
                              ]
                             )
                             for item in tree_constituents
                    ]
    
    return processed_tree
    
def print_sentence_tree(sentence_tree):
    

    processed_tree = process_sentence_tree(sentence_tree)
    processed_tree = [
                        Tree( item[0],
                             [
                                 Tree(x[1], [x[0]])
                                 for x in item[1]
                             ]
                            )
                            for item in processed_tree
                     ]

    tree = Tree('S', processed_tree )
    print tree
    
def visualize_sentence_tree(sentence_tree):
    
    processed_tree = process_sentence_tree(sentence_tree)
    processed_tree = [
                        Tree( item[0],
                             [
                                 Tree(x[1], [x[0]])
                                 for x in item[1]
                             ]
                            )
                            for item in processed_tree
                     ]
    tree = Tree('S', processed_tree )
    tree.draw()
    
    
t = create_sentence_tree(sentence)
print t

pt = process_sentence_tree(t)
pt

print_sentence_tree(t)
visualize_sentence_tree(t)