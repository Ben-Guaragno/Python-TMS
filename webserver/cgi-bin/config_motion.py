#!/home/ben/python/venv/bin/python3

import os
import urllib.parse
import requests

def wrapped_get(s):
    try:
        r=requests.get(s)
        return str(r.status_code)+": "+r.text
    except Exception as e:
        return str(e)

#Get query string and apply action to Motion
query_string=os.environ['QUERY_STRING']
args=urllib.parse.parse_qs(query_string)

if "set" in args.keys():
    if args["set"][0]=='Stop':
        arg_motion='Stop'
        wrapped_get("http://localhost:8081/0/action/quit")
    elif args["set"][0]=='Start':
        arg_motion='Start'
        wrapped_get("http://localhost:8081/0/detection/start")
    elif args["set"][0]=='Pause':
        arg_motion='Pause'
        wrapped_get("http://localhost:8081/0/detection/pause")
    elif args["set"][0]=='Restart':
        arg_motion='Restart'
        wrapped_get("http://localhost:8081/0/action/restart")
    else:
        arg_motion=None
else:
    arg_motion=None

#Get Motion status
motion_cur_status_str=""
if not arg_motion:
    motion_cur_status=wrapped_get("http://localhost:8081/0/detection/status")
    motion_cur_status_str="<p><b>Motion status:</b> "+motion_cur_status+"</p>"

#Print out if email setting updated
arg_motion_str=""
if arg_motion!=None:
    arg_motion_str="<p><b>Motion set to:</b> "+arg_motion+"</p>"

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<h1>Motion Config</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
<p><a href="/cgi-bin/config_motion.py">Raw reload</a></p>
<br>
{arg_motion_str}
{motion_cur_status_str}
<br>
<button onclick="window.location.href='/cgi-bin/config_motion.py?set=Pause';">
    Motion Pause
</button>
<button onclick="window.location.href='/cgi-bin/config_motion.py?set=Start';">
    Motion Start
</button>
<button onclick="window.location.href='/cgi-bin/config_motion.py?set=Stop';">
    Motion Stop
</button>
<button onclick="window.location.href='/cgi-bin/config_motion.py?set=Restart';">
    Motion Restart
</button>

</body>
</html>"""
)

