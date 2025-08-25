import os
import math
import random
import string
import time

# === Utility functions to generate filler noise ===
def useless_function(x):
    total = 0
    for i in range(100):
        total += math.sin(i) * x
    return total

def another_useless(x):
    return [c for c in str(x) if c.isdigit()]

def random_string(length=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def print_banner():
    print("=" * 40)
    print("     Welcome to the Fake App")
    print("=" * 40)

# Some random global variables
USERS = ["alice", "bob", "charlie"]
MAX_RETRIES = 5
CACHE = {}

# === First fake secret ===
AWS_ACCESS_KEY_ID = "AKIAFAKE1234567890FAKE"

def connect_db():
    # Noise computations
    noise = useless_function(42)
    print("Noise value:", noise)

    # === Second fake secret (buried deeper) ===
    DB_PASSWORD = "P@ssw0rd123!"
    print("Connecting to DB with password:", DB_PASSWORD)

    return {"connected": True}

def generate_noise_data(n=50):
    data = []
    for i in range(n):
        item = {
            "id": i,
            "value": random_string(10),
            "number": random.randint(100, 999)
        }
        data.append(item)
    return data

def compute_series(limit=30):
    results = []
    for i in range(1, limit):
        results.append((i, i**2, i**3))
    return results

# Some placeholder processing
def process_users(users):
    for u in users:
        print("Processing user:", u)
        time.sleep(0.01)

# === Third fake secret ===
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEKEY1234"

def meaningless_loop():
    s = 0
    for i in range(1000):
        s += i % 13
    return s

def fake_logger(msg):
    print("[DEBUG]", msg)

# === Fourth fake secret (pretend API key) ===
FAKE_API_KEY = "12345-ABCDE-FAKE-SECRET-67890"

def noisy_function():
    arr = []
    for i in range(1, 200):
        arr.append(i * random.randint(1, 10))
        if i % 10 == 0:
            fake_logger("Checkpoint " + str(i))
    return arr

def do_some_calculations():
    total = 0
    for i in range(1, 500):
        total += (i * i) % 7
    return total

# === Fifth fake secret ===
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEArandomfakekeytestpayloadthatlookslikeRSA==
-----END RSA PRIVATE KEY-----"""

def display_menu():
    print("\nOptions:")
    print("1. Connect DB")
    print("2. Generate Noise")
    print("3. Compute Series")
    print("4. Exit")

def main():
    print_banner()
    retries = 0

    while retries < MAX_RETRIES:
        display_menu()
        choice = random.randint(1, 4)  # fake choice for noise
        print("Auto-selected option:", choice)

        if choice == 1:
            connect_db()
        elif choice == 2:
            data = generate_noise_data(5)
            print("Generated data:", data)
        elif choice == 3:
            series = compute_series(10)
            print("Series:", series)
        elif choice == 4:
            print("Exiting...")
            break

        retries += 1
        time.sleep(0.1)

    fake_logger("Run finished with " + str(retries) + " iterations")
    print("Meaningless loop result:", meaningless_loop())
    print("Noise calc:", do_some_calculations())

# === Sixth fake secret ===
STRIPE_TEST_KEY = "sk_test_51H8FAKEKEY1234567890ABCDEFGHIJKL"

if __name__ == "__main__":
    main()
