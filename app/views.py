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
	r = requests.get(url)

	while r.status_code is not 200:
	        r = requests.get(url)
	
	soup = BeautifulSoup(r.text)
	titles = soup.find_all("title")
	size = len(titles)
	matches = []
	for match in range(size):
	    if len(set(titles[match].text.split(" ")).intersection(set(teams))) > 0:
	    	matches.append(titles[match].text)
	return '''
<html>
  <head>
    <title>Live IPL Score</title>
  </head>
  <body>
    <h1>''' + '<br>'.join(matches) + '''</h1>
  </body>
</html>
'''
    
