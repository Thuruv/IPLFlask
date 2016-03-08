from flask import render_template
from app import app
import requests
from bs4 import BeautifulSoup

       
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',go='here')


@app.route('/hindu')
def hindu():
    r = requests.get('http://www.thehindu.com/opinion/editorial/')
    soup = BeautifulSoup(r.text)
    for i in soup.find_all('h1'):
            for j in i.find_all('a'):
                    x = j['href']
            r2 = requests.get(x)
            soup = BeautifulSoup(r2.text)
            news =  [i.text for i in soup.find_all("p")]
            r = 'https://www.readability.com/api/content/v1/parser?url=' + ''.join(news) + '&token=b92b64e6e68f9614d87102bcccc726debe1feba0'
            c = requests.get(r)
    return render_template('test.html',title = soup.title, content=news)

@app.route('/thindu')
def tamil_hindu():
    base_link = 'http://tamil.thehindu.com/opinion/editorial/?service=rss'
    c = requests.get(base_link)
    soup = BeautifulSoup(c.text)
    news = (soup.find('item').text).strip()
    #news = 'http://www.thehindu.com/opinion/editorial/jat-reservation-stir-unreasonable-demands/article8264631.ece?utm_source=RSS_Feed&amp;utm_medium=RSS&amp;utm_campaign=RSS_Syndication'
    r = 'https://www.readability.com/api/content/v1/parser?url=' + news + '&token=b92b64e6e68f9614d87102bcccc726debe1feba0'
    c = requests.get(r)
    return render_template('test.html',go=c.json()['content'])

@app.route('/test')
def test():
  #return render_template('page_backup.html')
  return render_template('test.html')
