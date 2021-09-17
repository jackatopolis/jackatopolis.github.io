import numpy as np
import pymongo
from flask import Flask, jsonify, render_template,redirect,url_for,request,make_response

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.jackDB
db.info.drop()

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    from webscrape import scrape
    data = scrape()
    
    return data

@app.route('/', methods=['GET','POST'])
def home():
    from webscrape import scrape
    if request.method == 'POST':
        datafromjs = request.form['mydata']
        data = scrape()
        db.info.insert_one(data)
        out = list(db.info.find())
        resp = make_response(data)
        return resp
        return render_template('index.html', out=out)


if __name__ == '__main__':
    app.run(debug=True)