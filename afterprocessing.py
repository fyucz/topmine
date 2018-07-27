# -*- coding: utf-8 -*-
num_topics = 2 ##改这里!

dic_vocab = {}
with open('input/seg_index.txt', 'r', encoding='utf-8') as r_file:
    lines = r_file.readlines()
for line in lines:
    _list = line.strip().split()
    index = _list[0]
    vocab = _list[-1]
    dic_vocab[index] = vocab

for topic_index in range(0,num_topics):
    topic_file_name = 'output/topic'+str(topic_index)+'.txt'
    with open(topic_file_name,'r',encoding='utf-8') as topic_file:
        lines = topic_file.readlines()
    with open(topic_file_name, 'w', encoding='utf-8') as topic_file:
        for line in lines:
            segs_index = line.strip().split()[:-1]
            count = line.strip().split()[-1]
            segs = [dic_vocab[index] for index in segs_index]
            segs.append(count)
            topic_file.write(' '.join(segs) + '\n')
        topic_file.close()

with open('output/frequent_phrases.txt','r',encoding='utf-8') as frequent_file:
    lines = frequent_file.readlines()
with open('output/frequent_phrases.txt','w',encoding='utf-8') as frequent_file:
    for line in lines:
        _temp = line.strip().split("'")
        indexs = _temp[1].strip().split()
        segs = [dic_vocab[index] for index in indexs]
        _temp[1] = ' '.join(segs)
        _line = "'".join(_temp)
        frequent_file.write(_line + '\n')
    frequent_file.close()

print('afterprocessing enc ...')