import time
import random
import redis
import string

conn = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    val = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    conn.set("keyval", val)

    val = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    conn.rpush("somelist", val)

    val = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    num = random.randint(1, 10)
    conn.zadd("sortedset", num, val)

    val = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    conn.sadd("regset", val)
    time.sleep(1)
