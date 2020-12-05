import hashlib
import sys


def read_key(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()


def mine(secret_key):
    
    idx = 1
    running = True
    match = None
    
    while running:
        base = "%s%d" % (secret_key, idx)
        hh = hashlib.md5(base.encode("utf-8")).hexdigest()
        if hh.startswith("00000"):
            match = base
            break
        idx += 1
    return match


if __name__ == "__main__":
    k = read_key(sys.argv[-1])
    coin = mine(k)
    print("%s" % (coin,))
            