#!/home/ben/python/venv/bin/python3

import time

#22 char per line

def read_data(num_lines):
    f=open("/home/ben/python/data.csv",'r')
    f.seek(0,2)
    total_chars=f.tell()
    start=total_chars-22*num_lines
    if start<0:
        start=0
    f.seek(start)

    l=[]
    for x in f:
        parts=x.split(',')
        tf=float(parts[0])
        rh=float(parts[1])
        tmstamp=int(parts[2])
        l+=(tf,rh,tmstamp)

    return l

def read_data_pretty(num_lines):
    l=read_data(num_lines)
    out_l=[]
    for tf,rh,tmstamp in zip(*[iter(l)]*3):
        tf_str="%0.1f F"  % tf
        rh_str="%0.1f %%" % rh
        t_str=time.strftime("%I:%M%p %m/%d/%y", time.localtime(tmstamp))
        out_l+=(tf_str,rh_str,t_str)
    return out_l

if __name__ == '__main__':
    print(read_data(1))
    print(read_data(50))
    print(read_data_pretty(2))
