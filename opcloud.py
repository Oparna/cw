from flask import Flask, render_template, request, jsonify
import json
import requests
from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel


cluster = Cluster(['cassandra'])
session = cluster.connect()


app = Flask(__name__)

url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_callingcode = 'https://restcountries.eu/rest/v2/callingcode/{callingcode}'
url_city = 'https://restcountries.eu/rest/v2/capital/{capital}'

# This route is the initial route that the user goes to login and enter the homepage.  
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'user' or request.form['password'] != 'user':
			error = 'The credentials entered are incorrect!'
		else:
			return render_template('homepage.html')
		return jsonify(response)
	#return render_template('loginpage.html', error=error)

@app.route('/homepage',  methods=['GET', 'POST'])
def home():
	return render_template('homepage.html')

#Method to specify whether it is POST or GET. This allows you to enter a country name. If it doesnt exist then error code appears
@app.route('/name',  methods=['GET', 'POST'])
def name_country():
	# This is to get the data, in this case to get the country name entered
    url = url_name.format(name=request.form.get('name'))
    response = requests.get(url)
	# If it doesn't exists then return the following text, 404 specifies which error code.
    if response.status_code == 404:
        return "<h1>Error, page does not exist!</h1>", 404
    response = response.json()
    return jsonify(response)
    #return render_template('backg.html', result = response)
	
#Method to specify whether it is POST or GET. This allows you to enter a calling code. If it doesnt exist then error code appears (404). 
#The return is a json format, although a html format is available but hashed out currently. 
@app.route('/callingcode',  methods=['GET', 'POST'])
def callcode():
    url = url_callingcode.format(callingcode=request.form.get('callingcode'))
    response = requests.get(url)
    if response.status_code == 404:
        return "<h1>Error, page does not exist!</h1>", 404
    response = response.json()
    return jsonify(response)
    #return render_template('backg.html', result = response, par="Code {}".format(request.form.get('callingcode')))
	
#Method to specify whether it is POST or GET. This allows you to enter a capital city. If it doesnt exist then error code appears (404)
@app.route('/city',  methods=['GET', 'POST'])
def capcity():
	url = url_city.format(capital=request.form.get('city'))
	response = requests.get(url)
	if response.status_code == 404:
		return "<h1>Error, page does not exist!</h1>", 404
	response = response.json()
	return jsonify(response)
	#return render_template('backg.html', result = response, par="cityname {}".format(request.form.get('city')))


# In order to run the app this is needed
if __name__=="__main__":
    app.run(port=8080, debug=True)
