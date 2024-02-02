#!/home/ben/python/venv/bin/python

import subprocess
import time
import smtp_email

t=time.localtime()
t_str=time.strftime("%I:%M%p %m/%d/%y", t)

res=subprocess.run(['sudo apt update | grep -v W:'], capture_output=True, text=True, shell=True)
#print(res)
#print("***************")
#print(res.stdout)

body=t_str+"\n\n"+res.stdout

if 'apt list --upgradable' in res.stdout:
    s='apt list --upgradable'
    updatable_res=subprocess.run([s], capture_output=True, text=True, shell=True)
    body+="\n\n"+updatable_res.stdout

smtp_email.send_email("Pi Update Check", body)
