#!/home/ben/python/venv/bin/python

import subprocess, socket
import time
import smtp_email

def main():

    t=time.localtime()
    t_str=time.strftime("%I:%M%p %m/%d/%y", t)

    i=0
    SLEEP_TIME=10 #seconds
    while True:
        is_internet=internet_check()

        if is_internet:
            #internet
            break
        else:
            #no internet
            i+=1
            if i*SLEEP_TIME>=60*3:
                #3 min timeout
                s=time.strftime("%I:%M%p %m/%d/%y", time.localtime())+": Internet check failed"
                s+=". Reboot email was not sent."
                s='echo "'+s+'" >> /home/ben/internet_checks.txt'
                res=subprocess.run([s], capture_output=True, text=True, shell=True)
                exit(0)
        time.sleep(SLEEP_TIME)

    body=t_str+"\nRaspberry Pi Zero W booted"
    if i>0:
        body+="\nInternet available after "+str(i*SLEEP_TIME)+" seconds"
    smtp_email.send_email("Pi Boot Notification", body)

def internet_check(host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            #print(ex)
            return False

if __name__ == '__main__':
    main()
