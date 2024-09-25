# Rabbit MQ Python script setup
A quick way to test Rabbit MQ features with python. This setup contains 3 Rabbit MQ servers running in a Consumer - Producer setup. 

### Requirements
- python 3
- docker
- docker-compose

### Setup
##### create virtual environment
```
python -m venv venv
```
##### Install Rabbit MQ connector package
```
pip install pika
```
##### Run the Rabbit MQ Servers
```
docker-compose up -d
```
##### Run Consumers (1 Consumer is enough)
```
python consumer-1.py
```
```
python consumer-2.py
```

##### Run Producers
```
python producer.py
```



### Dashboard Access
```
https://localhost:8080
```

##### enter default credentials 
```
user: guest
password: guest
```