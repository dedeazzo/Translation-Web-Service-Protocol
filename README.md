# Translation-Web-Service-Protocol
Simple Flask API protocol for translation web service

## RUNNING FLASK APP

**>>** set FLASK_APP=app

**>>** set FLASK_ENV=development

**>>** flask run

_Note: use 'export' instead of 'set' for Linux_


## FUNCTIONS
Interacting with API using curl 

**Get value for language id and key**

**Format:** {language_id: key}

**Run:** curl -i http://127.0.0.1:5000/get -X GET -H "Content-Type: application/json" -d "{\"en\": \"buy-chips\"}"


**Create new translation**

**Format:** {language_id: {key: key_value, ...}}

**Run:** curl -i http://127.0.0.1:5000/put -X PUT -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"


**Add translation**

**Format:** {language_id: {key: key_value, ...}}

**Run:** curl -i http://127.0.0.1:5000/post -X POST -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"
