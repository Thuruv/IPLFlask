from flask import render_template
from app import app
import requests
from bs4 import BeautifulSoup

url = "www.tehelka.com/2015/12/it-is-unfair-to-judge-nehru-on-kashmir-shashi-tharoor/"

@app.route('/')
@app.route('/index')
def index():
	r = requests.get(url)

	while r.status_code is not 200:
	        r = requests.get(url)
	
	soup = BeautifulSoup(r.text)
	matches.append(soup.title)
	return '''
        <html>
          <head>
            <title>zxxx</title>
          </head>
          <body>
            <h1>''' + '<br>'.join(matches) + '''</h1>
          </body>
        </html>
        '''
    
