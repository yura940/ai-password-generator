# ai_password_generator/main.py

import string
import random
import numpy as np
from collections import defaultdict

ALL_CHARS = string.ascii_letters + string.digits + string.punctuation
EPISODES = 10000
EPSILON = 0.1
ALPHA = 0.5
GAMMA = 0.9

# --- Ask for password length in English ---
while True:
    try:
        MAX_LEN = int(input("Choose password length (6, 8 or 12): "))
        if MAX_LEN in [6, 8, 12]:
            break
        else:
            print("❌ Please choose only 6, 8 or 12.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

# --- Reward Functions ---
def is_weak(pwd):
    weak_patterns = ["123", "abc", "password", "qwerty", "111"]
    return any(p in pwd.lower() for p in weak_patterns)

def get_reward(pwd):
    reward = 0
    if any(c.isdigit() for c in pwd): reward += 1
    if any(c.islower() for c in pwd): reward += 1
    if any(c.isupper() for c in pwd): reward += 1
    if any(c in string.punctuation for c in pwd): reward += 1
    if len(set(pwd)) > 6: reward += 1
    if len(pwd) >= 8: reward += 2
    if is_weak(pwd): reward -= 5
    return reward

# --- Q-Learning ---
Q = defaultdict(float)

for episode in range(EPISODES):
    pwd = ""
    for step in range(MAX_LEN):
        state = pwd
        if random.random() < EPSILON:
            action = random.choice(ALL_CHARS)
        else:
            q_vals = [Q[(state, a)] for a in ALL_CHARS]
            max_q = max(q_vals)
            best_actions = [a for a, q in zip(ALL_CHARS, q_vals) if q == max_q]
            action = random.choice(best_actions)

        next_pwd = pwd + action
        reward = get_reward(next_pwd)
        future_q = max([Q[(next_pwd, a)] for a in ALL_CHARS]) if len(next_pwd) < MAX_LEN else 0

        Q[(state, action)] += ALPHA * (reward + GAMMA * future_q - Q[(state, action)])
        pwd = next_pwd

# --- Generation ---
def generate_password():
    pwd = ""
    for _ in range(MAX_LEN):
        q_vals = [Q[(pwd, a)] for a in ALL_CHARS]
        max_q = max(q_vals)
        best_actions = [a for a, q in zip(ALL_CHARS, q_vals) if q == max_q]
        action = random.choice(best_actions)
        pwd += action
    return pwd

# --- Execution ---
if __name__ == "__main__":
    print("\nGenerated Passwords:\n")
    for _ in range(10):
        print(generate_password())

