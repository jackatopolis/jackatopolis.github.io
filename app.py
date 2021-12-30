import numpy as np
import pymongo
from flask import Flask, jsonify, render_template,redirect,url_for,request,make_response
import webscrape as ws

#testData = scrape()
data = ws.scrapeData()

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html', out=data)


# @app.route('/update', methods=['POST'])
# def update():
#     data = scrape()
#     return jsonify({"jsdata": data})



if __name__ == '__main__':
    app.run(debug=True)