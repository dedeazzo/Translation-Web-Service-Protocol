import requests
import pandas as pd
from flask import Flask, request, jsonify
import json
import pickle
import psycopg2

app = Flask(__name__)

#trans_template = {
#    'en': {"buy-chips": 'Buy chips', "buy-fries": 'Buy fries'},
#    'fr': {"fr-chips": 'french fries'},
#}

# Connect to db
#conn = psycopg2.connect(host="localhost", port = 5432, database="translate", user="postgres", password="postgres") 
#cur = conn.cursor()

# Read table
#details = pd.read_sql_query("SELECT * FROM translation.lang_table;", conn)


# get from dict
# {'en': 'buy-chips'}
# curl -i http://127.0.0.1:5000/get -X GET -H "Content-Type: application/json" -d "{\"en\": \"buy-chips\"}"
@app.get('/get')
def query_records():
    if request.is_json:
        name = request.get_json()
        #name = json.load(str(request.get_json()))
        with open('persistent_store.txt', 'rb') as f:
            data = f.read()
            data = pickle.loads(data)
            # get reguested language and values from store
            in_lang = list(name.keys())[0]
            ln = data.get(in_lang)
            # if language is None return error
            if ln == None:
                return jsonify({'error': 'data not found'}), 204
            # get value of translation key requested from dict 
            # of translation keys in requested language
            out_trans = (ln.get(in_lang)).get(name.get(in_lang))
            if out_trans != None:
                return jsonify({'output': out_trans}), 200
            return jsonify({'error': 'data not found'}), 204
    return {"error": "Request must be JSON"}, 415


# new dict
# {'en': {'buy-chips': 'Buy chips', ...}}
# curl -i http://127.0.0.1:5000/put -X PUT -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"
@app.put('/put')
def create_record():
    if request.is_json:
        #record = json.loads(request.data)
        record = request.get_json()
        in_lang = list(record.keys())[0]
        data = {}
        data[in_lang] = record
        with open('persistent_store.txt', 'wb') as f:
            pickle.dump(data, f)
        return jsonify(record), 202
    return {"error": "Request must be JSON"}, 415

# add to dict
# {'en': {'buy-chips': 'Buy chips', ...}}
# curl -i http://127.0.0.1:5000/post -X POST -H "Content-Type: application/json" -d "{\"en\": {\"buy-chips\": \"Buy chips\"}}"
@app.post('/post')
def update_record():
    if request.is_json:
        record = request.get_json()
        with open('persistent_store.txt', 'rb') as f:
            data = f.read()
            data = pickle.loads(data)
            in_lang = list(record.keys())[0]

            # check if file is empty
            if not f.read(1):
                data = {}
            # if lang does not exist
            if not in_lang in data.keys():
                data[in_lang] = record
            else:
                # get values of language from store, merge with new translations and update
                tr = data[in_lang]
                tr.update(record[in_lang])
                data[in_lang] = tr
        with open('persistent_store.txt', 'wb') as f:
            pickle.dump(data, f)
        return jsonify(record), 202
    return {"error": "Request must be JSON"}, 415

app.run(debug=True)