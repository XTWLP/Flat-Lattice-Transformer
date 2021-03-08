#!usr/bin/env python
# encoding: utf-8

from paths import weibo_ner_path
import os

def deseg_weibo(weibopath):
    train_path = os.path.join(weibopath, 'weiboNER_2nd_conll.train')
    dev_path = os.path.join(weibopath, 'weiboNER_2nd_conll.dev')
    test_path = os.path.join(weibopath, 'weiboNER_2nd_conll.test')

    for data_file in [train_path, dev_path, test_path]:
        output_file = data_file + "_deseg"
        f_out = open(output_file, "w", encoding='utf8')
        with open(data_file, "r", encoding='utf8') as f:
            for line in f.readlines():
                line = line.strip()
                if line != "":
                    span_list = line.split('\t')
                    raw_char = ''.join(list(span_list[0])[:-1])
                    tag = span_list[-1]
                    f_out.write(' '.join([raw_char, tag]) + '\n')
                else:
                    f_out.write('\n')

if __name__ == '__main__':
    deseg_weibo(weibo_ner_path)
    print('- Done!')
