#!/home/ben/python/venv/bin/python3

import subprocess
from html_formatter import html_format

s='sudo apt update | grep -v W:'
res=subprocess.run([s], capture_output=True, text=True, shell=True)

if 'apt list --upgradable' in res.stdout:
    upgr_str='<br><a href="/cgi-bin/list_upgradable.py">View updates?</a></p><br>'
else:
    upgr_str=''

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<h1>Executed apt update</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
{upgr_str}
<p><b>stdout:</b> {html_format(res.stdout)}</p>
<p><b>stderr:</b> {html_format(res.stderr.strip())}</p>
<p><b>Return Code:</b> {res.returncode}</p>
</body>
</html>"""
)

