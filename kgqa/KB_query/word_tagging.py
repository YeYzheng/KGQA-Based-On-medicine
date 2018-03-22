# encoding=utf-8

"""

@desc: 定义Word类的结构；定义Tagger类，实现自然语言转为Word对象的方法。

"""

import jieba
import jieba.posseg as pseg


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class Tagger:
    def __init__(self, dict_paths):
        # TODO 加载外部词典
        for p in dict_paths:
            jieba.load_userdict(p)

        # TODO jieba不能正确切分的词语，我们人工调整其频率。
        jieba.suggest_freq(('特征','症状','症候'),True)

    @staticmethod
    def get_word_objects(sentence):
        # type: (str) -> list
        """
        把自然语言转为Word对象
        :param sentence:
        :return:
        """
        return [Word(word.encode('utf-8'), tag) for word, tag in pseg.cut(sentence)]

# TODO 用于测试
if __name__ == '__main__':
    tagger = Tagger(['./external_dict/jibing_name.txt', './external_dict/drug_name.txt'])
    #while True:
    s = '喉插管损伤需要什么药治疗？'
    for i in tagger.get_word_objects(s):
        print(i.token.decode('utf-8'), i.pos)
