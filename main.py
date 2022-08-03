
from flask import Flask
from flask import jsonify
from flask import request
import pika
import argparse
import os
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--rabbit_ip", help="Redis IP address")
parser.add_argument("-rp", "--redis_port", type=str, help="Redis Port number", default="5672")
parser.add_argument("-q", "--queue", default="hello", help="Redis queue name")
parser.add_argument("-p", "--app_port", default="3000", help="Define application port, default: 3000")
args = vars(parser.parse_args())


USER = os.getenv('USER', 'user')
PASSWORD = os.getenv('PASSWORD','user')
RABBIT_IP = args["rabbit_ip"]
QUEUE_NAME = args["queue"]
APP_PORT = args["app_port"]
REDIS_PORT = args["redis_port"]
app = Flask(__name__)
credentials = pika.PlainCredentials(USER, PASSWORD)

def func(x):
	return x + 1

def test_naswer():
	assert func(3) == 4


def conenction_up():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBIT_IP,heartbeat=0,credentials=credentials))
    channel = connection.channel()
    return channel


@app.route('/add', methods=['POST'])
def test_post():
    try:
        request_data2 = request.get_data(request.get_json())
        channel.queue_declare(queue=QUEUE_NAME)
        channel.basic_publish(exchange='', routing_key='hello', body=request_data2)
        return jsonify(result="OK"), 200
    except pika.exceptions.ChannelWrongStateError:
        conenction_up()


if __name__ == '__main__':
    print ("Lacze sie do")
    print (RABBIT_IP)
    channel = conenction_up()
    app.run(host='0.0.0.0',port=APP_PORT)
