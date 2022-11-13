import redis
import random

# redis_server = redis.Redis() # создание подключения
# redis_server.close() # закрытие соединения
with redis.Redis() as redis_server: # позволяет закрывать автоматически
    redis_server.lpush("queue", random.randint(0, 10)) # вставка (push) слева (l), queue - название очереди, 1 - значение для вставки в очередь 

