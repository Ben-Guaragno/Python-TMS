#!/home/ben/python/venv/bin/python3

import board, adafruit_ahtx0
import time

sensor = adafruit_ahtx0.AHTx0(board.I2C())
c_temp=sensor.temperature
f_temp=c_temp*9/5+32
rh=sensor.relative_humidity

temp_f_string="%0.1f" % f_temp
rh_string="%0.1f" % rh

time_raw=time.time()
time_int=int(time_raw)

#Ensure values are always 4 chars
#Truncates if >99         (101.5 -> 0101)
#Adds leading zero if >10 (  9.4 -> 09.4)
def len_fixer(s):
    if len(s)>4:
        s=s[:-2]
    if len(s)<4:
        s='0'+s
    return s

temp_f_string=len_fixer(temp_f_string)
rh_string=len_fixer(rh_string)
time_formatted=time.strftime("%-I:%M%p", time.localtime(time_int))

w_str=temp_f_string+','+rh_string+','+time_formatted

print(
    f"""\
Content-Type: text/plain

{w_str}
"""
)

