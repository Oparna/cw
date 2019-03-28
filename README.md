
# APPLICATION
> This application allows you to search a country but its name, calling code, and capital city.
##  List of API
```python
url_name = 'https://restcountries.eu/rest/v2/name/{name}'
url_callingcode = 'https://restcountries.eu/rest/v2/callingcode/{callingcode}'
url_city = 'https://restcountries.eu/rest/v2/capital/{capital}'
```

## Explanation
```
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

The next section was then done on google cloud

Set region and zone set for the new cluster:
gcloud config set compute/zone europe-west2-b 
export PROJECT_ID="$(gcloud config get-value project -q)
	 
Cassandra in Kubernetes section command:
gcloud container clusters create cassandra --num-nodes=3 --
machine-type "n1-standard-2" 		  		
	 
Downloaded using these command:
wget -O cassandra-peer-service.yml http://tinyurl.com/yyxnephy 
wget -O cassandra-service.yml http://tinyurl.com/y65czz8e
wget -O cassandra-replication-controller.yml http://tinyurl.com/y2crfsl8
	
Then run using these commands:
kubectl create -f cassandra-peer-service.yml 
kubectl create -f cassandra-service.yml 
kubectl create -f cassandra-replication-controller.yml

Got name of our cassandra container:
kubectl get pods -l name=cassandra
	 
Check that the ring has been formed between all of the  Cassandra instances:
kubectl exec -it cassandra-sk9m6 -- nodetool status
	
Copied my data from the previous section: 
kubectl cp data.csv cassandra-sk9m6:/oparna.csv 
	
Then run cqlsh inside the container: 
kubectl exec -it cassandra-sk9m6 cqlsh 
	
Built a keyspace using this command: 
CREATE KEYSPACE data WITH REPLICATION {'class' : 'SimpleStrategy', 'replication_factor' : 2};
	
Created the table for my stats and ingest the CSV via copy:
	CREATE TABLE data.stats (Name text PRIMARY KEY, Capital_City text, ) ;
	COPY oparna.stats(Name,Capital_City) FROM 'oparna.csv' WITH DELIMITER=',' AND HEADER=TRUE;
	
Built the image:
docker build -t gcr.io/${PROJECT_ID}/oparna-app:v1 .

At this point there were some issues with the docker image. When the next steps were attempted there were errors.

```
```  
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
 Afghanistan |        Kabul
	
```python
	# This route is the initial route that the user goes to login.
	@app.route('/', methods=['GET', 'POST'])

	#Method to specify whether it is POST or GET
	request.method == 'POST'

	# In order to the POST data
	request.form['username']

	# The error code that appears when the page does not exist
	if response.status_code == 404:


```
