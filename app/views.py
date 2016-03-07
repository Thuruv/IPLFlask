from flask import render_template
from app import app
import requests
from bs4 import BeautifulSoup

url = "http://static.cricinfo.com/rss/livescores.xml"
teams = (
    "Chennai", "Delhi",
    "Punjab", "Kolkata",
    "Mumbai", "Rajasthan",
    "Bangalore", "Hyderabad"
    )
        
@app.route('/')
@app.route('/index')
def index():
        r = requests.get('http://www.thehindu.com/opinion/editorial/')
        soup = BeautifulSoup(r.text)
        for i in soup.find_all('h1'):
                for j in i.find_all('a'):
                        x = j['href']
                r2 = requests.get(x)
                soup = BeautifulSoup(r2.text)
                y =  [i.text for i in soup.find_all("p")]
	return '''
<html>
  <head>
    <title>Live IPL Score</title>
  </head>
  <body>
  <h1>''' + '<br>'.join(soup.title) + '''</h1>
    <p>''' + '<br>'.join(y) + '''</p>
  </body>
</html>
'''


