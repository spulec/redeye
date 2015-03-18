import sys
import time

import redis


def get_vals_for_key(conn, key):
    redis_type = conn.type(key)
    if redis_type == 'string':
        count = 1
        vals = conn.get(key)
    elif redis_type == 'list':
        count = conn.llen(key)
        vals = conn.lrange(key, 0, 2)
    elif redis_type == 'set':
        count = conn.scard(key)
        vals = conn.srandmember(key, 3)
    elif redis_type == 'zset':
        count = conn.zcard(key)
        vals = conn.zrange(key, 0, 2)
    else:
        print "Got unknown type {}".format(redis_type)
    return redis_type, count, vals


def check_keys(conn):
    keys = conn.keys()
    print(chr(27) + "[2J")
    for key in keys:
        key_type, count, vals = get_vals_for_key(conn, key)
        print '{0: <20} {1: <10} {2: <5} {3}'.format(key, key_type, count, vals)


def main():
    conn = redis.StrictRedis(host='localhost', port=6379, db=9)

    if '--reset' in sys.argv:
        if conn.connection_pool.connection_kwargs['host'] == 'localhost':
            conn.flushdb()
        else:
            assert False, "Tried to reset on non-localhost"

    while True:
        check_keys(conn)
        time.sleep(1)


if __name__ == '__main__':
    main()
