from flask import Flask
from flask import jsonify
from flask import request
import pika


IP_ADDRES = "192.168.0.13"
PORT_REDIS = 6379
QUEUE_NAME = 'hello'

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def test_post():
    request_data2 = request.get_data(request.get_json())
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=IP_ADDRES))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_publish(exchange='', routing_key='hello', body=request_data2)
    connection.close()
    return jsonify(result="OK"), 200


app.run(port=3000)