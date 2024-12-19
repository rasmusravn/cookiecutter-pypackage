#!/usr/bin/python3

import subprocess

try:
    subprocess.call(["hatch", "env", "create"])
    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", "Initial commit"])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
