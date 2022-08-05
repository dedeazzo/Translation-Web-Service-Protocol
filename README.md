# Translation-Web-Service-Protocol
Simple Flask API protocol for translation web service

## RUNNING FLASK APP

><code>set FLASK_APP=app</code>

><code>set FLASK_ENV=development</code>

><code>flask run</code>

*Note: use 'export' instead of 'set' for Linux*


## FUNCTIONS
Interacting with API using curl 

#### Get value for language id and key

*Format: {language_id: key}*

><code>curl -i http://127.0.0.1:5000/get -X GET -H "Content-Type: application/json" -d "{\"en\": \"buy-chips\"}"</code>


#### Create new translation

*Format: {language_id: {key: key_value, ...}}*

><code>curl -i http://127.0.0.1:5000/put -X PUT -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"</code>


#### Add translation

*Format: {language_id: {key: key_value, ...}}*

><code>curl -i http://127.0.0.1:5000/post -X POST -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"</code>
