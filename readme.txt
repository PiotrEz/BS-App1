Application 1 Help:

positional arguments:
  i                     Redis IP address

options:
  -h, --help            show this help message and exit
  -rp REDIS_PORT, --redis_port REDIS_PORT
                        Redis Port number
  -q QUEUE, --queue QUEUE
                        Redis queue name
  -p APP_PORT, --app_port APP_PORT
                        Define application port, default: 3000


Application 2 Help:

positional arguments:
  --ip_redis IP_REDIS   Redis IP address
  --ip_rabbitmq IP_RABBITMQ
                        RabbitMQ IP address
                        
options:                     
  -q QUEUE, --queue QUEUE
                        Redis queue name
  -p APP_PORT, --app_port APP_PORT
                        Define application port
  -rp REDIS_PORT, --redis_port REDIS_PORT
                        Redis Port
  -rmp RABBITMQ_PORT, --rabbitmq_port RABBITMQ_PORT
                        RabbitMQ Port
  -t TTL, --TTL TTL     Define TTL, default: 60
  -rmqu RABBITMQ_USER, --rabbitmq_user RABBITMQ_USER
                        Define RabbitMQ user name
  -rmqp RABBITMQ_PASSWORD, --rabbitmq_password RABBITMQ_PASSWORD
                        Define RabbitMQ user password


Application 3 Help:

positional arguments:
  i                     Database IP address

options:
  -h, --help            show this help message and exit
  -pr PORT_REDIS, --port_redis PORT_REDIS
                        Redis Database Port
  -p PORT, --port PORT  Set application port


STEP BY STEP: (Moze się zmienić adres IP! Wykorzystać komendę powyżej)

1.Start Rabbit MQ  --- RabbitMQ IP: 172.17.0.2

docker run --rm -it -p 15672:15672 -p 5672:5672 --net bs-app rabbitmq:3.10-management 

2. App 1 - Przyjmuje post i laczy sie z RabbitMQ. ---- App1 IP: 172.17.0.3

docker run -p 3000:3000 --net bridge 17417ccea7ba 172.17.0.2


3. Start Redis -- Redis IP: 172.17.0.4

docker run -p 6379:6379 --name redis --net bs-app  redis



4. App 2 - Laczy sie z Rabbit MQ oraz z redisem

docker run --net bridge 99b56b19863a --ip_redis=172.17.0.4 --ip_rabbitmq=172.17.0.2

5. App 3 - Laczy sie z Redisem.

docker run --net bridge b576d25baf50 172.17.0.4





docker inspect -f '{{ .NetworkSettings.IPAddress }}' - Ładnie wyświetla numer IP wewnątrz kontenera.


docker network inspect bridge -- Pokazuje yamla z calej sieci bridge.











