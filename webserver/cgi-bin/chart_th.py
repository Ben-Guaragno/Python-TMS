#!/home/ben/python/venv/bin/python3

import sys
sys.path.append("/home/ben/python")
import read_data

UP_ARROW="&uarr;"
DOWN_ARROW="&darr;"

data=read_data.read_data(49)
labels=""
tdata=""
hdata=""
for tf,rh,tmstamp in zip(*[iter(data)]*3):
    labels+="new Date("+str(tmstamp)+"000),"
    tdata+="%0.1f," % tf
    hdata+="%0.1f," % rh

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

<div><canvas id="chart"></canvas></div>

<script>
document.getElementById("referralLink").innerHTML='<a href="' + document.referrer + '">Back to Options</a>';
</script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.0/Chart.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.13.0/moment.min.js"></script>

<script>
var color = ["#ff6384", "#5959e6"]

var config = {{
  type: 'line',
  data: {{
    labels: [{labels[:-1]}],
    datasets: [{{
      label: "Temp",
      backgroundColor: "transparent",
      borderColor: color[0],
      pointBackgroundColor: color[0],
      pointBorderColor: color[0],
      pointHoverBackgroundColor: color[0],
      pointHoverBorderColor: color[0],
      data: [{tdata[:-1]}],
    }},
    {{
      label: "Humidity",
      backgroundColor: "transparent",
      borderColor: color[1],
      pointBackgroundColor: color[1],
      pointBorderColor: color[1],
      pointHoverBackgroundColor: color[1],
      pointHoverBorderColor: color[1],
      data: [{hdata[:-1]}],
    }}
    ]
  }},
  options: {{
    scales: {{
      xAxes: [{{
        type: 'time',
      	time: {{
          unit: 'minute',
          unitStepSize: 15,
  	      displayFormats: {{
          'minute': 'h:mma'
          }}
        }}
      }}],
    }},
  }}
}};

var ctx = document.getElementById("chart").getContext("2d");
new Chart(ctx, config);
</script>

</body>
</html>"""
)

