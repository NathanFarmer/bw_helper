import os
import subprocess
import re
import sys

def login():
    user = os.environ['BW_USER']
    password = os.environ['BW_PASS']

    login = f'bw login {user} {password}'
    result = subprocess.run(login, text=True, shell=True, check=True, capture_output=True)

    if result.returncode == 0:
        output = result.stdout.strip()

    try:
        bw_session = re.search('export BW_SESSION="(.+?)"', output).group(1)
    except:
        subprocess.run('bw logout', text=True, shell=True, check=True)
        sys.exit(1)

    os.environ['BW_SESSION'] = bw_session

def get_password(item):
    get_password = f'bw get password {item}'
    return subprocess.run(get_password, text=True, shell=True, capture_output=True)

def logout():
    logout = 'bw logout'
    subprocess.run(logout, text=True, shell=True, check=True)
