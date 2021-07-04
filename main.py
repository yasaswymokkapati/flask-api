from flask import Flask, jsonify, request
import csv

all_articles = []
with open('articles.csv') as f:
    data = csv.reader(f)
    data = list(data)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)
@app.route('/get_articles')

def get_articles():
    return jsonify({
        'data' : all_articles[0],
        'status' : 'success'
    })

@app.route('/liked_articles', methods = ['POST'])
@app.route('/disliked_articles', methods = ['POST'])

def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    articles_liked.append(article)
    return jsonify({
        'status' : 'success'
    }), 210

def dislike_articles():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(movie)
    return jsonify({
        'status' : 'success'
    }), 420
    
if __name__ == '__main__':
    app.run()