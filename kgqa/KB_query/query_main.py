# encoding=utf-8

"""
@desc:main函数，整合整个处理流程。
"""
from KGQA_Based_On_medicine.settings import fuseki,q2s

def query_function(question):


        while True:
            question = question
            #print(question.encode('utf-8'))
            #isinstance(question.encode('utf-8'))
            my_query = q2s.get_sparql(question.encode('utf-8'))
            #print(my_query)
            if my_query is not None:
                result = fuseki.get_sparql_result(my_query)
                value = fuseki.get_sparql_result_value(result)

                # TODO 查询结果为空，根据OWA，回答“不知道”
                if len(value) == 0:
                    return 'Yso还小，知识库中并没有该问题的答案！！！'
                elif len(value) == 1:
                    print(len(value[0]))
                    if len(value[0]) != 1:
                        return value[0]
                    else:
                        return value[0]
                else:
                    output = ''
                    for v in value:
                        output += v + u'、'
                    return output

            else:
                # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
                return 'Yso还小，无法理解你的问题！！！'

            #print('#' * 100)

if __name__ == '__main__':
    while True:
        question = input('请输入你的问题：')
        #print(question.encode('utf-8'))
        #isinstance(question.encode('utf-8'))
        my_query = q2s.get_sparql(question.encode('utf-8'))
        #print(my_query)
        if my_query is not None:
            result = fuseki.get_sparql_result(my_query)
            value = fuseki.get_sparql_result_value(result)

            # TODO 判断结果是否是布尔值，是布尔值则提问类型是"ASK"，回答“是”或者“不知道”。
            if isinstance(value, bool):
                if value is True:
                    print('Yes')
                else:
                    print('I don\'t know. :(')
            else:
                # TODO 查询结果为空，根据OWA，回答“不知道”
                if len(value) == 0:
                    print('I don\'t know. :(')
                elif len(value) == 1:
                    print(len(value[0]))
                    print(value[0])
                else:
                    output = ''
                    for v in value:
                        output += v + u'、'
                    print(output)

        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            print('I can\'t understand. :(')

        print('#' * 100)

