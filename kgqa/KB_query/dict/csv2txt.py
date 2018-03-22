# encoding=utf-8

"""

@author: SimmerChan

@contact: hsl7698590@gmail.com

@file: jena_sparql_endpoint.py

@time: 2017/12/20 17:42

@desc:
把从mysql导出的csv文件按照jieba外部词典的格式转为txt文件。
nz代表专名，本demo主要指电影名称。
nr代表人名。

"""
import pandas as pd
def csv_to_txt():
    df = pd.read_csv('./movie_title.csv')
    title = df['movie_title'].values

    with open('./movie_title.txt', 'a') as f:
        for t in title[1:]:
            f.write(t + ' ' + 'nz' + '\n')

def put_pos():
    pos_d = open('./symptom_pos.txt','a',encoding='utf-8')
    f = open('./symptom_name.txt','r',encoding='utf-8')
    drug_name = f.read().split('\n')
    f.close()
    for i in drug_name:
        pos_d.write(i + ' ' + 'nz' + '\n')
    pos_d.close()

    # f = open('./jibing_name.txt','r',encoding='utf-8')
    # pos_j = open('./jibing_pos_name.txt','a',encoding='utf-8')
    # jibingname = f.read().split('\n')
    # f.close()
    # for i in jibingname:
    #     pos_j.write(i + ' ' + 'nj' + '\n')
    # pos_j.close()





if __name__ == '__main__':
    put_pos()
