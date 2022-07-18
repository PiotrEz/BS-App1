from flask import Flask
from flask import jsonify
from flask import request
import pika
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("i", help="Redis IP address")
parser.add_argument("-q", "--queue", default="hello", help="Redis queue name")
parser.add_argument("-p", "--app_port", default="3000", help="Define application port, default: 3000")
args = vars(parser.parse_args())

RABBIT_IP = args["i"]
QUEUE_NAME = args["queue"]
APP_PORT = args["app_port"]

app = Flask(__name__)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBIT_IP))
channel = connection.channel()


@app.route('/add', methods=['POST'])
def test_post():
    request_data2 = request.get_data(request.get_json())
    channel.queue_declare(queue=QUEUE_NAME)
    channel.basic_publish(exchange='', routing_key='hello', body=request_data2)
    return jsonify(result="OK"), 200


app.run(port=APP_PORT)

