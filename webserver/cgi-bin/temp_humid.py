#!/home/ben/python/venv/bin/python3

import board, adafruit_ahtx0

sensor = adafruit_ahtx0.AHTx0(board.I2C())
c_temp=sensor.temperature
f_temp=c_temp*9/5+32
rh=sensor.relative_humidity

temp_f_string="%0.1f F" % f_temp
rh_string="%0.1f %%" % rh

print(
    f"""\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" href="/styles.css?get" type="text/css">
</head>
<body>
<h1>Temperature and Humidity</h1>
<br>
<p id="referralLink"></p>
<br>
<table>
    <tr>
        <th>Temperature</th>
        <th>Humidity</th>
    </tr>
    <tr>
        <td>{temp_f_string}</td>
        <td>{rh_string}</td>
    </tr>
</table>

<script>
document.getElementById("referralLink").innerHTML='<a href="' + document.referrer + '">Back to Options</a>';
</script>

</body>
</html>"""
)

