"""
@desc: 为每个问题设定语义模板
"""
from refo import finditer, Predicate, Star, Any, Disjunction
import re
import random




# TODO SPARQL前缀和模板
SPARQL_PREXIX = u"""
PREFIX : <http://www.kgdrug.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""
SPARQL_SELECT_TEM = u"{prefix}\n" + \
             u"SELECT DISTINCT {select} WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n"

class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        # 正则表达式
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token.decode('utf-8'))
        m2 = self.pos.match(word.pos)
        return m1 and m2

class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action
        self.condition_num = random.random()

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])

        return self.action(matches), self.condition_num

class QuestionSet:
    def __init__(self):
        pass
    #todo 疾病
    @staticmethod
    def has_zhengzhuang_question(word_objects):
        """
        某疾病有什么症状？
        :param word_objects:
        :return:
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :haszhengzhuang ?m." \
                    u"?m :zzname ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_bingfazheng_question(word_objects):
        '''
        并发症
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :bingfazheng ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_yufang_question(word_objects):
        '''
        预防
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :yufang ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_gaishu_question(word_objects):
        '''
        疾病概述
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :gaishu ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_zhiiao_question(word_objects):
        '''
        疾病治疗
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :zhiliao ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    #todo 药品
    @staticmethod
    def has_gnzhzh_question(word_objects):
        '''
        药品疗效
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_drug:
                e = u"?s :proname '{person}'." \
                    u"?s :gazhzh ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_pzwh_question(word_objects):
        '''
        药品批准文号
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_drug:
                e = u"?s :proname '{person}'." \
                    u"?s :pzwh ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    #todo 症状
    @staticmethod
    def has_sympotm_gaishu_question(word_objects):
        '''
        症状概述
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_symptom:
                e = u"?s :zzname '{person}'." \
                    u"?s :zzgaishu ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_sympotm_yufang_question(word_objects):
        '''
        症状预防
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_symptom:
                e = u"?s :zzname '{person}'." \
                    u"?s :zzyufang ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def has_disease_to_drug_question(word_objects):
        '''
        症状预防
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_disease:
                e = u"?s :jibingname '{person}'." \
                    u"?s :needcure ?m." \
                    u"?m :proname ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def has_symptom_to_disease_question(word_objects):
        '''
        症状预防
        :param word_objects:
        :return:
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == pos_symptom:
                e = u"?s :zzname '{person}'." \
                    u"?s :relatedisease ?m." \
                    u"?m :jibingname ?x".format(person=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql



# TODO 定义关键词
# 药品、疾病词性
pos_drug = 'nd'
pos_disease = 'nj'
pos_symptom = 'nz'
drug_entity = (W(pos=pos_drug))
disease_entity = (W(pos=pos_disease))
symptom_entity = (W(pos=pos_symptom))
#问题关键词
zhengzhuang_keyword = (W('症状')|W('症候')|W('特征'))
bingfazheng_keyword = (W('病发症')|W('并发症'))
yufang_keyword = (W('预防')|W('预防措施'))
gaishu_keyword = (W('概述'))
zhiliao_keyword = (W('治')|W('治疗')|W('治疗措施'))
gnzhzh_keyword = (W('功效')|W('疗效')|W('用处')|W('用'))
pzwh_keyword = (W('批准文号')|W('文号'))
disease_drug_keyword = (W('药')|W('药品')|W('药治')|W('药治疗'))
symptom_disease_keyword = (W('病')|W('疾病'))
#规则集合
rules = [
    Rule(condition_num=2,condition=disease_entity + Star(Any(),greedy=False) + zhengzhuang_keyword + Star(Any(),greedy=False),action=QuestionSet.has_zhengzhuang_question),
    Rule(condition_num=2,condition=disease_entity + Star(Any(),greedy=False) + bingfazheng_keyword + Star(Any(),greedy=False),action=QuestionSet.has_bingfazheng_question),
    Rule(condition_num=2,condition=disease_entity + Star(Any(),greedy=False) + yufang_keyword + Star(Any(),greedy=False),action=QuestionSet.has_yufang_question),
    Rule(condition_num=2,condition=disease_entity + Star(Any(),greedy=False) + gaishu_keyword + Star(Any(),greedy=False),action=QuestionSet.has_gaishu_question),
    Rule(condition_num=2,condition=disease_entity + Star(Any(), greedy=False) +zhiliao_keyword,action=QuestionSet.has_zhiiao_question),
    Rule(condition_num=2,condition=Star(Any(),greedy=False) + yufang_keyword + disease_entity,action=QuestionSet.has_yufang_question),
    Rule(condition_num=2,condition=Star(Any(),greedy=False) + zhiliao_keyword + disease_entity,action=QuestionSet.has_zhiiao_question),

    Rule(condition_num=2,condition=drug_entity + Star(Any(),greedy=False) + gnzhzh_keyword +  Star(Any(),greedy=False) ,action=QuestionSet.has_gnzhzh_question),
    Rule(condition_num=2,condition=drug_entity + Star(Any(),greedy=False) + pzwh_keyword + Star(Any(),greedy=False),action=QuestionSet.has_pzwh_question),

    Rule(condition_num=2,condition=symptom_entity + Star(Any(),greedy=False) + gaishu_keyword + Star(Any(),greedy=False),action=QuestionSet.has_sympotm_gaishu_question),
    Rule(condition_num=2,condition=symptom_entity + Star(Any(),greedy=False) + yufang_keyword + Star(Any(),greedy=False),action=QuestionSet.has_sympotm_yufang_question),
    Rule(condition_num=2,condition=Star(Any(),greedy=False) + yufang_keyword + symptom_entity,action=QuestionSet.has_sympotm_yufang_question),

    Rule(condition_num=2,condition=disease_entity + Star(Any(),greedy=False)  + disease_drug_keyword + (Star(Any(),greedy=False)|disease_entity),action=QuestionSet.has_disease_to_drug_question),
    Rule(condition_num=2,condition=Star(Any(),greedy=False) + disease_drug_keyword + Star(Any(),greedy=False) + disease_entity,action=QuestionSet.has_disease_to_drug_question),
    Rule(condition_num=2,condition=symptom_entity + Star(Any(),greedy=False) + symptom_disease_keyword,action=QuestionSet.has_symptom_to_disease_question),

]