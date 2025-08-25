import math
import random
import string

def rand_str(n=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def checksum(data):
    return sum(ord(c) for c in data) % 256

# === First fake secret ===
STRIPE_SECRET_KEY = "sk_test_51H8FAKEKEY1234567890ABCDEFGHIJKL"

def noisy_math(n=50):
    res = []
    for i in range(n):
        res.append(math.sin(i) + math.cos(i))
    return res

def dummy_cache(data):
    cache = {}
    for i, d in enumerate(data):
        cache[i] = checksum(d)
    return cache

# === Second fake secret ===
TWILIO_AUTH_TOKEN = "fAkeAuThT0ken1234567890abcdef"

def fake_encrypt(msg, key="default"):
    return ''.join(chr((ord(c) + len(key)) % 256) for c in msg)

def fake_decrypt(msg, key="default"):
    return ''.join(chr((ord(c) - len(key)) % 256) for c in msg)

def big_noise():
    numbers = []
    for i in range(100):
        numbers.append((i, i*i, rand_str(5)))
    return numbers

# === Third fake secret ===
AWS_SESSION_TOKEN = "FwoGZXIvYXdzEFAaDJFAKESESSIONTOKEN1234567890"

def log_noise():
    for i in range(20):
        if i % 5 == 0:
            print("Log checkpoint", i)

def meaningless_series(n=10):
    return [i**3 - i**2 for i in range(n)]

# === Fourth fake secret ===
FAKE_API_KEY = "AIzaSyD-FAKEKEY-1234567890abcdefghijklmnopqr"

def simulate_load():
    for i in range(100):
        _ = math.sqrt(i) * random.randint(1, 50)

if __name__ == "__main__":
    data = [rand_str(6) for _ in range(10)]
    cache = dummy_cache(data)
    print("Cache:", cache)
    print("Noise:", noisy_math(20))
    print("Decrypt test:", fake_decrypt(fake_encrypt("hello")))
    print("Big noise:", big_noise())
    log_noise()
