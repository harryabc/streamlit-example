from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
from ddparser import DDParser
ddp = DDParser()
import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


title = st.text_input('搜索', '保障性租赁住房')

genre = st.radio('你需要什么，宝宝？',('关键词top10', '词云图','简化版文件'))

if genre=='关键词top10':
    h=open("实验1.txt","r",encoding='utf-8').read()
    keys=analyse.extract_tags(h)
    num1=1
    for key in keys:
        if num1<=10:
            st.write(key,num1)
            
            num1+=1
        else:
            continue


    def yuchuli(x):
        ls=''
        for line in x:  #打开文件
            rs = line.rstrip('\n')  # 移除行尾换行符
          # 输出移除后的行
            ls+=rs
        return ls
    def fenju(x):#x is 'xxxx。xxxxx。xxxx....'
        x=x.split('。')
        
        return x
    def juhao(w):
        s=ddp.parse(w)
        if s==None:
            st.write('')
        else:    
            d=s[0]
            z=0
            d1=d['word']
            d2=d['head']
            d3=d['deprel']
            
            
            for e in d3:
                if e=='，'or e==',':
                    z+=1
                if e=='HED':
                    st.write(d1[d3.index(e)])
                    for i2 in d1:
                        if i2=='，' or i2==',':
                            z-=1
                        elif z==0 and i2=='，':
                            z-=1
                        elif z==0 and i2==',':
                            z-=1
                        elif z==0:
                            st.write(i2,end='')
                            
                        else:
                            continue
                    
                    
    o=open("实验3.txt","r",encoding='utf-8').read()
    o=fenju(yuchuli(o))
    for o1 in o:
        juhao(o1)
        st.write('')

        
    ag_, token.dep_, token.head.text, token.head.tag_))



else:
        # 958条评论数据
    with open('实验1.txt','r',encoding='utf-8') as f:
        data = f.read()

    # 文本预处理  去除一些无用的字符   只提取出中文出来
    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
    new_data = " ".join(new_data)

    # 文本分词
    seg_list_exact = jieba.cut(new_data, cut_all=True)

    result_list = []
    with open('stop_word.txt', encoding='utf-8') as f:
        con = f.readlines()
        stop_words = set()
        for i in con:
            i = i.replace("\n", "")   # 去掉读取每一行数据的\n
            stop_words.add(i)

    for word in seg_list_exact:
        # 设置停用词并去除单个词
        if word not in stop_words and len(word) > 1:
            result_list.append(word)
    print(result_list)

    # 筛选后统计
    word_counts = collections.Counter(result_list)
    # 获取前100最高频的词
    word_counts_top100 = word_counts.most_common(100)
    print(word_counts_top100)

    # 绘制词云
    my_cloud = WordCloud(
        background_color='white',  # 设置背景颜色  默认是black
        width=900, height=600,
        max_words=100,            # 词云显示的最大词语数量
        font_path='simhei.ttf',   # 设置字体  显示中文
        max_font_size=99,         # 设置字体最大值
        min_font_size=16,         # 设置子图最小值
        random_state=50           # 设置随机生成状态，即多少种配色方案
    ).generate_from_frequencies(word_counts)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # 显示生成的词云图片
    plt.imshow(my_cloud, interpolation='bilinear')
    # 显示设置词云图中无坐标轴
    #plt.axis('off')
    #plt.show()
    st.pyplot()






