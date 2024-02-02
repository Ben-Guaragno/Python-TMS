import json

CONFIG_FILE="/home/ben/python/.config"

def read(k=None):
    with open(CONFIG_FILE, 'r') as f:
        json_str=f.readline()
        try:
            config=json.loads(json_str)
        except:
            config={}

        if isinstance(k,str) and k not in config.keys():
            config[k]='F'
        return config

def write(d):
    with open(CONFIG_FILE, 'w') as f:
        f.write(json.dumps(d))
