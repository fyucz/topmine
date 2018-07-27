# -*- coding: utf-8 -*-
import jieba
set_word = set()
with open('input/train.txt','r',encoding='utf-8') as r_file:
    lines = r_file.readlines()
    for line in lines:
        segs = list(jieba.cut(line.strip()))
        for seg in segs:
            set_word.add(seg)
list_word = list(set_word)
dic_vocab = {}
with open('input/seg_index.txt', 'w', encoding='utf-8') as w_file:
    for index,seg in enumerate(list_word):
        dic_vocab[seg] = index
        w_file.write(str(index)+ ' ' + seg + '\n')
    w_file.close()

with open('input/train.txt','r',encoding='utf-8') as r_file:
    lines = r_file.readlines()
    with open('input/dblp_5k.txt','w',encoding='utf-8') as w_file:
        for line in lines:
            segs = list(jieba.cut(line.strip()))
            index_word = []
            for seg in segs:
                index_word.append(str(dic_vocab[seg]))
            w_file.write(' '.join(index_word) + '\n')
        w_file.close()
print("processing end ...")