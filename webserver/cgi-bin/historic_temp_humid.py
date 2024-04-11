#!/home/ben/python/venv/bin/python3

import sys
import os, urllib.parse
sys.path.append("/home/ben/python")
import read_data

#Get the query string
query_string=os.environ['QUERY_STRING']
args=urllib.parse.parse_qs(query_string)

#Initialize the options for the select menu
options=[]
options+=["<option value=\"12hr\">12 Hours</option>"]
options+=["<option value=\"24hr\">24 Hours</option>"]
options+=["<option value=\"2d\">2 Days</option>"]

hrs_read=12    #time span to read, in hours
#Sets hrs_read, and selects the option indicated by tspan
if "tspan" in args.keys():
    if args["tspan"][0]=='24hr':
        hrs_read=24
        options[1]=options[1][:7]+" selected=\"selected\" "+options[1][8:]
    elif args["tspan"][0]=='2d':
        hrs_read=24*2
        options[2]=options[2][:7]+" selected=\"selected\" "+options[2][8:]
    else:
        #12hr and anything else
        hrs_read=12
        options[0]=options[0][:7]+" selected=\"selected\" "+options[0][8:]

# HTML codes for arrows. Not used presently
# UP_ARROW="&uarr;"
# DOWN_ARROW="&darr;"

#4 reads per hour, plus one more so it starts/ends at the same time
data_reads=hrs_read*4+1
data=read_data.read_data_pretty(data_reads)
html_str=""
#Format data into HTML table rows
for tf,rh,tmstamp in zip(*[iter(data)]*3):
    html_str="<tr><td>"+tf+"</td><td>"+rh+"</td><td>"+tmstamp+"</td></tr>\n"+html_str
#Add headers to HTML table
html_str="<tr><th>Temperature</th><th>Humidity</th><th>Timestamp</th></tr>\n"+html_str

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css?v=5" type="text/css">
</head>
<body>
<h1>Temperature and Humidity</h1>
<br>
<table style="width: 100%;"><tr>
<td><a href="/index_example.html">Back to Options</a></td>
<td align="right">
    <form action="/cgi-bin/historic_temp_humid.py" method="get">
    <select name="tspan" id="tspan" onchange="this.form.submit()">
        {options}
    </select>
    </form>
</td>
</tr></table>
<br>
<table class="thformat">
    {html_str}
</table>

</body>
</html>"""
)

