#!/home/ben/python/venv/bin/python3

import subprocess
from html_formatter import html_format

s='apt list --upgradable'
res=subprocess.run([s], capture_output=True, text=True, shell=True)

list=res.stdout.split('\n')
colored_stdout=''
for x in list:
    if '/' in x:
        i=x.index('/')
        first=x[:i:]
        last=x[i::]
        colored_stdout+='<span class="dark_green">'+first+'</span>'+last
    else:
        colored_stdout+=x
    colored_stdout+='\n'

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<h1>Executed apt list --upgradable</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
<p><b>stdout:</b> {html_format(colored_stdout)}</p>
<p><b>stderr:</b> {html_format(res.stderr.strip())}</p>
<p><b>Return Code:</b> {res.returncode}</p>
</body>
</html>"""
)

