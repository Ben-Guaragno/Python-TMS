#!/home/ben/python/venv/bin/python

import time
import smtp_email
import read_data
import config

def main():
    t=time.localtime()
    t_str=time.strftime("%I:%M%p %m/%d/%y", t)

    #Check if emailing enabled
    is_email=config.read("EMAIL_HISTORIC_TH")["EMAIL_HISTORIC_TH"]
    if is_email=='F':
        #Emailing not enabled, stop
        print("Stopping")
        return

    data=read_data.read_data_pretty(8)
    body="Historic temperature and humidity\n[retrieved %s]\n\n" % t_str
    body+="Temperature | Humidity | Timestamp\n"
    body_data=""
    flag=False
    for tf,rh,tmstamp in zip(*[iter(data)]*3):
        if float(tf[:-2])<70:
            flag=True
            tf="*"+tf
        body_data="\t%10s | \t%7s | %s\n" % (tf,rh,tmstamp) + body_data


    body+=body_data

    subject="Scheduled T&H Data"
    if flag:
        subject="WARNING T&H Data"
    smtp_email.send_email(subject, body)


if __name__ == '__main__':
    main()
