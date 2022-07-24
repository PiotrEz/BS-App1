#!/bin/bash


NUMBER_RMQ=$(docker run -d -p 15672:15672 -p 5672:5672 --net bridge rabbitmq:3.10-management)
RABBIT_IP=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' ${NUMBER_RMQ}) 
echo "To jest IP rabbita: ${RABBIT_IP}"
echo "To jest RMQ Rabbita: ${NUMBER_RMQ}"

ID1=$(docker build -t bsapp1:hw7 -q ./BS-App1/BS-App1/)
NUMBER_APP1=$(docker run -d -p 3000:3000 --net bridge ${ID1} ${RABBIT_IP})
IP_APP1=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' ${NUMBER_APP1})

NUMBER_REDIS=$(docker run -d -p 6379:6379 --name redis --net bridge redis)
REDIS_IP=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' ${NUMBER_REDIS})


ID2=$(docker build -t bsapp2:hw7 -q ./BS-App2/BS-App2/)
NUMBER_APP2=$(docker run -d --net bridge ${ID2} --ip_redis=${REDIS_IP} --ip_rabbitmq=${RABBIT_IP})

ID3=$(docker build -t bsapp3:hw7 -q ./BS-App3/)
NUMBER_APP3=$(docker run -d -p 2500:2500 --net bridge ${ID3} ${REDIS_IP})
IP_APP3=$(docker inspect -f '{{ .NetworkSettings.IPAddress }}' ${NUMBER_APP3})

echo "IP App1: ${IP_APP1}"
echo "IP App3: ${IP_APP3}"


