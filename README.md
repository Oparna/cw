# APPLICATION
> This application allows you to search a country but its name, calling code, and capital city.
##  List of API
```python
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_callingcode = 'https://restcountries.eu/rest/v2/callingcode/{callingcode}'
url_city = 'https://restcountries.eu/rest/v2/capital/{capital}'
```

## Explanation
Open the command line and direct to where the app is
Next create a virtual environment:

python3 -m venv name_of_project
source name_of_project/bin/activate

Activate the virtual environment using this command:
source name_of_project/bin/activate

From app directory run this:
python -m pip install -U -r requirements.txt

To run the app use the following command (the python file name will depend on what your application is called):
python opcloud.py

If there are no errors then a link will appear on the terminal, clicking on this   will then take you to the the website:

* Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 287-256-339

To see the table created inside the google cloud use the command:

select * from oparna.stats; 

 name        | capital_city
-------------+--------------
    Malaysia | Kuala Lumpur
       China |      Beijing
        Fiji |         Suva
     England |       London
     Algeria |      Algiers
      France |        Paris
     Germany |       Berlin
 Afghanistan |        KabulV

```python
	# This route is the initial route that the user goes to login.
	@app.route('/', methods=['GET', 'POST'])

	#This is used to find method whether it is POST or GET
	request.method == 'POST'

	# In order to the POST data I do this
	request.form['username']

	# The error code that appears when the page does not exist, in our example this would be the case when a invalid country is entered.
	if response.status_code == 404:

	# returns a html response
	return render_template('background.html', result = response)


```
