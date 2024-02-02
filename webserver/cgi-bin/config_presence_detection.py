#!/home/ben/python/venv/bin/python3

import os
import urllib.parse
import sys
sys.path.append("/home/ben/python")
import config

#Read stored presence detection val
config_dict=config.read()
if "PRESENCE_DETECTION" in config_dict.keys():
    pres_det=config_dict["PRESENCE_DETECTION"]
else:
    pres_det='F'
    config_dict["PRESENCE_DETECTION"]='F'

if pres_det=='T':
    pres_det=True
else:
    pres_det=False
stored_pres_det=pres_det

#Get query string and apply to presence detection
query_string=os.environ['QUERY_STRING']
args=urllib.parse.parse_qs(query_string)

if "set" in args.keys():
    if args["set"][0]=='T':
        arg_pres_det=True
        pres_det=True
    elif args["set"][0]=='F':
        arg_pres_det=False
        pres_det=False
    else:
        arg_pres_det=None
else:
    arg_pres_det=None

arg_pres_det_str=""
if arg_pres_det!=None:
    arg_pres_det_str="<p><b>Presence detection set to:</b> "+str(pres_det)+"</p>"

if pres_det:
    config_dict["PRESENCE_DETECTION"]='T'
else:
    config_dict["PRESENCE_DETECTION"]='F'
config.write(config_dict)

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<h1>Presence Detection Config</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
<p><b>Current presence detection:</b> {stored_pres_det}</p>
{arg_pres_det_str}
<br>
<button onclick="window.location.href='/cgi-bin/config_presence_detection.py?set=T';">
    Presence Detection On
</button>
<button onclick="window.location.href='/cgi-bin/config_presence_detection.py?set=F';">
    Presence Detection Off
</button>

</body>
</html>"""
)

