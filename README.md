# Python App - Secret Scanning Test

This is a **fake Python application** designed for testing secret scanning tools like Gitleaks, TruffleHog, or GitHub Secret Scanning.  
All secrets in this repository are **dummy/fake** and intended solely for testing purposes.

---

## Features

- Noisy, multi-module Python project:
  - `app.py` - Main entry point
  - `config.py` - Configuration and environment setup
  - `utils.py` - Helper functions with filler code
  - `database.py` - Fake database access module
- Simulated secrets (AWS keys, DB passwords, API tokens, private keys) scattered across files.
- Filler code, loops, and junk functions to make manual detection harder.
- SQL dump `fakeapp_db.sql` included for testing database secret scanning.

---

## Requirements

- Python 3.9+
- No external dependencies required

---

## Installation

```bash
git clone https://github.com/fake-org/fake-python-app.git
cd fake-python-app
