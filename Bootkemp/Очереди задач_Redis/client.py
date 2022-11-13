import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop("queue") # brpop - взять справа и ждать, когда появится
print(int(value[1]))