import numpy as np
import pymongo
from flask import Flask, jsonify, render_template,redirect,url_for,request,make_response



app = Flask(__name__)

@app.route('/scrape')
def scrape():
    from webscrape import scrape
    data = scrape()
    return render_template('index.html', out=data)


@app.route('/')
def home():
    from webscrape import scrape
    data = scrape()
    return render_template('index.html', out=data)



if __name__ == '__main__':
    app.run(debug=True)