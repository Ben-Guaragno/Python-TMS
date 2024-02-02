import json

SECRETS_FILE="/home/ben/python/.secrets"

def read():
    with open(SECRETS_FILE, 'r') as f:
        json_str=f.read()
        try:
            secrets=json.loads(json_str)
        except:
            secrets={}

        return secrets

def write(d):
    with open(SECRETS_FILE, 'w') as f:
        f.write(json.dumps(d))
