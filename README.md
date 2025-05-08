# README.md

# 🔐 AI Password Generator

AI Password Generator is an intelligent Q-Learning-based generator that creates strong, secure, and diverse passwords using reinforcement learning.

Built for security-aware developers, pentesters, and cybersecurity enthusiasts.

---

## 🚀 Features

- 🤖 AI-driven password generation (Q-Learning)
- 🎯 Rewards based on complexity, diversity & length
- 🚫 Penalizes weak patterns like `123`, `abc`, `password`
- 🧪 Generates realistic passwords with optional randomness
- ✅ Simple to run — choose length and generate instantly

---

## 📦 Project Structure

```
main.py               # Main RL logic + generator
requirements.txt      # Dependencies
README.md             # This file
```
---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/yura940/ai-password-generator.git
cd ai-password-generator

# Setup environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
---

## ▶️ Usage

```bash
python main.py
```

---

## 📊 Reward Logic

| Feature              | Reward |
|----------------------|--------|
| Contains digits      | +1     |
| Contains lowercase   | +1     |
| Contains uppercase   | +1     |
| Contains symbols     | +1     |
| >6 unique chars      | +1     |
| ≥8 total length      | +2     |
| Weak patterns (123)  | -5     |

---

## 🛡️ Roadmap

- [x] Reinforcement-based password generator
- [ ] CLI flags `--count`, `--length`
- [ ] Save passwords to file
- [ ] Password strength scoring (zxcvbn)
- [ ] REST API / Web UI (Streamlit)

---

## 📛 Security Notice

This tool is meant for **learning and demonstration** purposes.  
Never store real secrets in generated datasets.

---

## 👨‍💻 Author

Built with 💻 on Kali Linux by [@yura940](https://github.com/yura940)  
Feel free to fork, star or contribute!

---
