import random
import string
import time

def fake_query(table, condition):
    return f"SELECT * FROM {table} WHERE {condition}"

def fake_insert(table, values):
    return f"INSERT INTO {table} VALUES ({','.join(values)})"

def noise_generator(n=50):
    return ["row_" + str(i) for i in range(n)]

# === First fake secret ===
POSTGRES_PASSWORD = "mysecretpassword"

class FakeDB:
    def __init__(self):
        self.connected = False
        self.data = {}

    def connect(self):
        # === Second fake secret (fake Mongo URI) ===
        MONGO_URI = "mongodb://user:fakepass@localhost:27017/test"
        self.connected = True
        print("Connected to Mongo with", MONGO_URI)

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

    def insert(self, key, value):
        self.data[key] = value
        print("Inserted:", key, value)

    def query(self, key):
        return self.data.get(key, None)

# Noise loops
def useless_numbers():
    out = []
    for i in range(200):
        out.append(i * i % 17)
    return out

# === Third fake secret ===
REDIS_PASSWORD = "redis_fake_password_1234"

def fake_backup(db):
    print("Backing up", len(db.data), "entries")
    time.sleep(0.05)

def fake_restore():
    print("Restoring backup...")
    time.sleep(0.05)

# === Fourth fake secret (looks like SSH key) ===
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABfakefakefake1234567890==
-----END OPENSSH PRIVATE KEY-----"""

def stress_test():
    for i in range(100):
        _ = (i * 3) % 5
        if i % 10 == 0:
            print("Test batch", i)

if __name__ == "__main__":
    db = FakeDB()
    db.connect()
    for i in range(10):
        db.insert("key" + str(i), "value" + str(i))
    print("Query result:", db.query("key5"))
    fake_backup(db)
    fake_restore()
    db.disconnect()
    print("Numbers:", useless_numbers()[:20])
    stress_test()
