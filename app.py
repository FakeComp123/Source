import os
import random
import math

# Some fake math utilities to add noise
def useless_function(x):
    total = 0
    for i in range(100):
        total += math.sin(i) * x
    return total

def another_useless(x):
    return [c for c in str(x) if c.isdigit()]

# Secrets mixed with junk variables
USER_LIST = ["alice", "bob", "charlie"]

AWS_ACCESS_KEY_ID = "AKIAFAKE1234567890FAKE"  # looks real
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAK_
