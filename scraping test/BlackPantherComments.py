from urllib.request import urlopen
from bs4 import BeautifulSoup
import string, re, jieba, numpy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def getFilmInfo(url):
    resp = urlopen(url)
    html_text = resp.read().decode('utf-8')
    bsObj = BeautifulSoup(html_text)
    nowPlayingList = bsObj.find_all('div', {'id' : 'nowplaying'})
    filmInfo = {}
    filmField = nowPlayingList[0].find_all('li', {'class': 'list-item'})[0]
    filmName = filmField.find('img')['alt']
    filmInfo['name'] = filmName
    filmId = getFilmId(filmField)
    filmInfo['id'] = filmId
    return filmInfo


def getFilmId(field):
    href = field.find('a', {'data-psource': 'title'})['href']
    filmId = str(href).strip('https://').split('/')[2]
    return filmId


def getComments(filmId, num):
    comments = []
    if num > 0:
        count = num * 20
    else:
        return False
    urlPath = 'https://movie.douban.com/subject/' + filmId + '/comments?start='+str(count)+'&limit=20&sort=new_score&status=P&percent_type='
    print(urlPath)
    resp = urlopen(urlPath)
    html = resp.read().decode('utf-8')
    bsObj = BeautifulSoup(html)
    commentsField = bsObj.find_all('div', {'class': 'comment-item'})
    print(commentsField)
    for item in commentsField:
        if item.find_all('p')[0].get_text() is not None:
            content = item.find_all('p')[0].get_text()
            comments.append(content)
    return comments


def generateImage(file):
    file = open('comments.txt', 'r', encoding='utf-8')
    comments = file.read()

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)

    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})

    stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='GBK')  # quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    print(words_df.head())
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"count": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["count"], ascending=False)

    matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
    # from wordcloud import WordCloud#词云包
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud = wordcloud.fit_words(dict(word_frequence_list))
    plt.imshow(wordcloud)
    plt.savefig('comments.jpg')


if __name__ == '__main__':
    commentsList = []
    filmId = getFilmInfo('https://movie.douban.com/cinema/nowplaying/chengdu/')['id']
    for i in range(10):
        num = i + 1
        comments_temp = getComments(filmId, num)
        commentsList.append(comments_temp)
    comments = ''
    for a in commentsList:
        comments += str(a).strip(string.punctuation)
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    comments = re.findall(pattern, comments)
    comments = ''.join(comments)
    file = open('comments.txt', 'w', encoding='utf-8')
    file.write(comments)
    generateImage(file)