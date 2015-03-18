import redis
import sure  # flake8:noqa

from redeye.main import get_vals_for_key


def test_get_vals_for_key():
    conn = redis.StrictRedis(host='localhost', port=6379, db=0)
    conn.flushdb()

    conn.set("keyval", "my-val")
    get_vals_for_key(conn, "keyval").should.equal(("string", 1, "my-val"))

    conn.rpush("somelist", "val1")
    conn.rpush("somelist", "val2")
    get_vals_for_key(conn, "somelist").should.equal(("list", 2, ["val1", "val2"]))

    conn.zadd("sortedset", 1, "val1")
    conn.zadd("sortedset", 2, "val2")
    conn.zadd("sortedset", 3, "val3")
    get_vals_for_key(conn, "sortedset").should.equal(("zset", 3, ["val1", "val2", "val3"]))

    conn.sadd("regset", "val1")
    conn.sadd("regset", "val2")
    get_vals_for_key(conn, "regset").should.equal(("set", 2, ["val1", "val2"]))
