#!flask/bin/python
# -- coding: utf-8 --
from flask import Flask, request
import json

from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/movies', methods=['GET'])
def movies():
    data = [
        {
            "id": 1,
            "name": "哥斯拉大战刚",
            "revenue": "275000000",
            "vote_average": "7.3",
            "vote_count": 1976
        },
        {
            "id": 2,
            "name": "鬼灭之刃之无限列车",
            "revenue": "190000000",
            "vote_average": "8.7",
            "vote_count": 2365
        },
        {
            "id": 3,
            "name": "尚气与十环传奇",
            "revenue": "320000000",
            "vote_average": "7.5",
            "vote_count": 3768
        },
        {
            "id": 4,
            "name": "真人快打",
            "revenue": "167060000",
            "vote_average": "6.3",
            "vote_count": 1122
        },
        {
            "id": 5,
            "name": "那些希望我死的人",
            "revenue": "131267370",
            "vote_average": "7.1",
            "vote_count": 364
        },
        {
            "id": 6,
            "name": "寂静之地 2",
            "revenue": "180500000",
            "vote_average": "7.4",
            "vote_count": 549
        },
        {
            "id": 7,
            "name": "活死人军团",
            "revenue": "97800000",
            "vote_average": "6.6",
            "vote_count": 1270
        },
        {
            "id": 8,
            "name": "人之怒",
            "revenue": "80437520",
            "vote_average": "7.7",
            "vote_count": 876
        },
        {
            "id": 9,
            "name": "小人物 Nobody",
            "revenue": "46088130",
            "vote_average": "8.5",
            "vote_count": 1796
        },
        {
            "id": 10,
            "name": "黑白魔女库伊拉",
            "revenue": "42600000",
            "vote_average": "8.8",
            "vote_count": 1574
        }
    ]

    return jsonify(data)
    # return json.dumps(data)


@app.route('/api/edit', methods=['POST'])
def edit():
    data1 = {
        'status': 200,
        'message': '修改成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)

@app.route('/api/add', methods=['POST'])
def add():
    data1 = {
        'status': 200,
        'message': '添加成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)

@app.route('/api/del', methods=['DELETE'])
def dele():
    data1 = {
        'status': 200,
        'message': '删除成功！！！',
        'data': {
            'parameter': {
                'order_id': 'sn12345'
            }
        }
    }
    return jsonify(data1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
