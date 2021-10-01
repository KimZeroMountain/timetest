from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
import time

time.time()
1586337535.9475923

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():

    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    reg_date = time.strftime('%Y.%m.%d %H:%M:%S')

    doc = {
        'title' : title_receive,
        'content' : content_receive,
        'reg_date' : reg_date
    }

    db.memo.insert_one(doc)


    return jsonify({'msg':'포스팅 성공!'})


@app.route('/post', methods=['GET'])
def get_post():
    memos = list(db.memo.find({}, {'_id': False}))

    return jsonify({'all_memo': memos})



@app.route('/delete_post', methods=['DELETE'])
def delete_post():
    delate_memo = request.form['title_give']

    db.memo.delete_one({'title': delate_memo})

    return jsonify({'msg': '삭제 성공!'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)