#!/home/ben/python/venv/bin/python3

import os
import urllib.parse
import sys
sys.path.append("/home/ben/python")
import config

#Read stored email setting
config_dict=config.read("EMAIL_HISTORIC_TH")

if config_dict["EMAIL_HISTORIC_TH"]=='T':
    is_email=True
else:
    is_email=False
stored_is_email=is_email

#Get query string and apply to email setting
query_string=os.environ['QUERY_STRING']
args=urllib.parse.parse_qs(query_string)

if "set" in args.keys():
    if args["set"][0]=='T':
        arg_is_email=True
        is_email=True
    elif args["set"][0]=='F':
        arg_is_email=False
        is_email=False
    else:
        arg_is_email=None
else:
    arg_is_email=None

#Print out if email setting updated
arg_is_email_str=""
if arg_is_email!=None:
    arg_is_email_str="<p><b>Emailing set to:</b> "+str(is_email)+"</p>"

#write value back to dict
if is_email:
    config_dict["EMAIL_HISTORIC_TH"]='T'
else:
    config_dict["EMAIL_HISTORIC_TH"]='F'
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
<h1>Email Historic T&H Config</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
<p><b>Current email setting:</b> {stored_is_email}</p>
{arg_is_email_str}
<br>
<button onclick="window.location.href='/cgi-bin/config_email_historic_th.py?set=T';">
    Email Historic T&H On
</button>
<button onclick="window.location.href='/cgi-bin/config_email_historic_th.py?set=F';">
    Email Historic T&H Off
</button>

</body>
</html>"""
)

