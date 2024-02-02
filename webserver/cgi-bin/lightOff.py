#!/home/ben/python/venv/bin/python3

import subprocess

s='echo 0 | sudo tee /sys/class/leds/ACT/brightness'
res=subprocess.run([s], capture_output=True, text=True, shell=True)

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<h1>Executed light off</h1>
<br>
<p><a href="/index_example.html">Back to Options</a></p>
<br>
<p><b>stdout:</b> {res.stdout}</p>
<p><b>stderr:</b> {res.stderr}</p>
<p><b>Return Code:</b> {res.returncode}</p>
</body>
</html>"""
)

