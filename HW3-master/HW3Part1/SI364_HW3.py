## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/artistinfo')
def artistinfohtml():
	x = request.args
	artisttoget = x.get('artist')
	theurl = "https://itunes.apple.com/search?term="
	newurl = theurl + str(artisttoget) 
	y = requests.get(newurl).text
	return render_template('artist_info.html', objects = json.loads(y)["results"])

@app.route('/artistlinks')
def artistlinkshtml():
    return render_template ("artist_links.html")

@app.route('/artistform')
def artistformhtml():
    return render_template('artistform.html')

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/specific/song/<artist_name>')
def specificsong(artist_name):
   the_url = "https://itunes.apple.com/search?term="
   new_url= the_url + str(artist_name)
   xx = requests.get(new_url).text
   return render_template("specific_artist.html", results = json.loads(xx) ["results"])


#done!

