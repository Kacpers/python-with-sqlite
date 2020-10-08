from repositories.urls import save, fetch_categories, fetch_urls
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    req = request.get_json()
    category = req['category']
    url = req['url']
    save(category, url)
    return {
        'status': 'ok'
    }

@app.route('/categories')
def get_categories():
    categories = fetch_categories()

    return jsonify([category[0] for category in categories])


@app.route('/category/<name>')
def get_category(name: str):
    urls = fetch_urls(name)

    return jsonify(urls)
