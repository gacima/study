# -*- coding: utf-8 -*-
import re, jieba, numpy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


file = open('comments.txt', 'r', encoding='utf-8')
comments = file.read()

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)
#print(cleaned_comments)

segment = jieba.lcut(cleaned_comments)
words_df = pd.DataFrame({'segment': segment})
#print(words_df)
stopwords=pd.read_csv("chineseStopWords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='GBK')#quoting=3全不引用
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
print(words_df.head())
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
#from wordcloud import WordCloud#词云包

wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80) #指定字体类型、字体大小和字体颜色
word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}
word_frequence_list = []
for key in word_frequence:
    temp = (key,word_frequence[key])
    word_frequence_list.append(temp)

wordcloud=wordcloud.fit_words(word_frequence_list)
plt.imshow(wordcloud)
