# Python-TMS
Python Temperature Monitoring System

Python scripts to read temperature data from a DHT20 connected to a Raspberry Pi Zero W. A Python Webserver facilitates on-demand access to data, as well as basic configuration options. SMTP emailing through Gmail is utilized for scheduled outbound data, which eliminates the need for port-forwarding and direct access to the Pi outside of the LAN.


### Crontab
Crontab is configured as below:
```
#Checks for updates every Sunday at 12:30am
30 */336 * * 0 python3 /home/ben/python/check_updates.py
#Send a reboot ack email
@reboot python3 /home/ben/python/reboot_ack.py
#Write data every 15 minutes
*/15 * * * * /home/ben/python/venv/bin/python3 /home/ben/python/write_data.py
#Try and email historic T&H data every 2 hours
5 */2 * * * python3 /home/ben/python/email_historic_th.py
```

### Start and Stop webserver

These commands will start and stop the webserver, which will run in the background after starting. Logs are written to the webserver_logs.txt file.

The webserver is **started** with the following command:
```bash
printf "$(date): Starting webserver\n">>webserver_logs.txt && python3 -m http.server 8080 --cgi -d python/webserver/ >>webserver_logs.txt 2>&1 &
```

The webserver is **stopped** with the following command:
```bash
pkill -9 python
printf "$(date): Webserver manually killed\n" >> webserver_logs.txt
```
