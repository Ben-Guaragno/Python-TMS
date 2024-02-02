#!/home/ben/python/venv/bin/python3

import sys
sys.path.append("/home/ben/python")
import read_data

UP_ARROW="&uarr;"
DOWN_ARROW="&darr;"

data=read_data.read_data_pretty(49)
html_str=""
for tf,rh,tmstamp in zip(*[iter(data)]*3):
    html_str="<tr><td>"+tf+"</td><td>"+rh+"</td><td>"+tmstamp+"</td></tr>\n"+html_str

html_str="<tr><th>Temperature</th><th>Humidity</th><th>Timestamp</th></tr>\n"+html_str

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css?get=1" type="text/css">
</head>
<body>
<h1>Temperature and Humidity</h1>
<br>
<p id="referralLink"></p>
<br>
<table>
    {html_str}
</table>

<script>
document.getElementById("referralLink").innerHTML='<a href="' + document.referrer + '">Back to Options</a>';
</script>

</body>
</html>"""
)

