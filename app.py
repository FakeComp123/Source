import os
import requests

# Fake AWS credentials
AWS_ACCESS_KEY_ID = "AKIAFAKE1234567890FAKE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEKEY1234"

# Fake database password
DB_PASSWORD = "P@ssw0rd123!"

def connect_db():
    print("Connecting to DB with password:", DB_PASSWORD)

if __name__ == "__main__":
    connect_db()
