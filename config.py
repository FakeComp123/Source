import os
import random
import string
import time

# Utility noise
def random_string(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def fake_delay():
    time.sleep(0.005)

# === First fake secret ===
GITHUB_TOKEN = "ghp_FAKE1234567890abcdefghijklmnopqrstu"

class Config:
    def __init__(self):
        self.debug = True
        self.retries = 3
        self.cache_enabled = False
        self.log_path = "/tmp/fakeapp.log"

    def summary(self):
        return {
            "debug": self.debug,
            "retries": self.retries,
            "cache": self.cache_enabled,
            "log_path": self.log_path
        }

# Noise functions
def generate_settings(n=20):
    return [{"id": i, "value": random_string(15)} for i in range(n)]

def display_settings(settings):
    for s in settings:
        print("Setting:", s["id"], s["value"])
        fake_delay()

# === Second fake secret (pretend Slack webhook) ===
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

def load_environment():
    env = {
        "HOME": os.getenv("HOME"),
        "PATH": os.getenv("PATH"),
        "DEBUG": str(True),
    }
    return env

def fake_loop():
    for i in range(50):
        if i % 10 == 0:
            print("Fake checkpoint", i)
        _ = i * i

# === Third fake secret ===
FAKE_DB_URI = "postgres://user:password@localhost:5432/fakedb"

def print_env(env):
    for k, v in env.items():
        print(f"{k}={v}")

def meaningless_computation():
    total = 0
    for i in range(200):
        total += (i * 3) % 7
    return total

# === Fourth fake secret ===
AZURE_STORAGE_KEY = "DefaultEndpointsProtocol=https;AccountName=fake;AccountKey=fakefakefake1234567890==;EndpointSuffix=core.windows.net"

if __name__ == "__main__":
    cfg = Config()
    print("Config summary:", cfg.summary())
    display_settings(generate_settings(5))
    env = load_environment()
    print_env(env)
    print("Computation:", meaningless_computation())
