from urllib.request import urlopen
from bs4 import BeautifulSoup
import string, re


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
    #file = open('comments.txt', 'w', encoding='utf-8')
    #file.write(comments)
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    comments = re.findall(pattern, comments)
    comments = ''.join(comments)

#getFilmInfo('https://movie.douban.com/cinema/nowplaying/chengdu/')
def cleanData():
    file = open('comments.txt')
