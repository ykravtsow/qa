#!/usr/bin/env python3
#coding: utf-8


import json
import sys
import os
from logging import Logger
from datetime import *


# combined log format parser
def parse_log(str):
    n = 1
    d = 0
    arr = []
    for line in str:
        # ip
        t1 = line.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in ip address part')
            d = d+1
            continue
        ip = line[:t1]
        tstr = line[t1+1:]

        # ident
        t1 = tstr.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in ident part')
            d = d+1
            continue
        id = tstr[:t1]
        tstr = tstr[t1+1:]

        # remote user
        t1 = tstr.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in remote user part')
            d = d+1
            continue
        ru = tstr[:t1]
        tstr = tstr[t1+2:]

        # timestamp
        t1 = tstr.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in timestamp part')
            d = d+1
            continue
        ts = tstr[:t1]
        tstr = tstr[t1+1:]

        # tzone
        t1 = tstr.find(']')
        if t1 == -1:
            l.error('error in line '+str(n)+' in time zone part')
            d = d+1
            continue
        tz = tstr[:t1]
        tstr = tstr[t1+3:]

        # request
        t1 = tstr.find('"')
        if t1 == -1:
            l.error('error in line '+str(n)+' in request part')
            d = d+1
            continue
        req = tstr[:t1]
        tstr = tstr[t1+2:]
        tl = req.split(' ')
        method = tl[0]
        prot = tl[len(tl)-1]
        url = ''
        for i in range(1, len(tl)-1):
            url = url+tl[i]+' '
        url = url[:-1]

        # status code
        t1 = tstr.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in status part')
            d = d+1
            continue
        sc = tstr[:t1]
        tstr = tstr[t1+1:]

        # size
        t1 = tstr.find(' ')
        if t1 == -1:
            l.error('error in line '+str(n)+' in resource size part')
            d = d+1
            continue
        sz = tstr[:t1]
        tstr = tstr[t1+2:]

        # referer
        t1 = tstr.find('"')
        if t1 == -1:
            l.error('error in line '+str(n)+' in referer part')
            d = d+1
            continue
        ref = tstr[:t1]
        tstr = tstr[t1+2:]

        # user-agent
        t1 = tstr.find('"')
        if t1 == -1:
            l.error('error in line '+str(n)+' in user-agent part')
            d = d+1
            continue
        ua = tstr[:t1]
        arr.append((ip, ts, method, url, sc))
        n = n+1

    return d, arr


def parse_logs(files):
    # concatenate files
    for l in files:
        b = []
        with open(l, 'r') as f:
            mylist = list(f)
            b = b + mylist
            return parse_log(b)


def get_stat_requests(r):
    requests = []
    stat = []
    for i in range(0, len(r)):
        if r[i][2] in requests:
            ind = requests.index(r[i][2])
            stat[ind]=stat[ind]+1
        else:
            requests.append(r[i][2])
            stat.append(1)
    # repack
    tmp = []
    for i in range(0, len(requests)):
        tmp.append((requests[i], stat[i]))
    return tmp


def second_sort(t):
    return t[1]


def get_top_ips(r):
    ips = []
    for i in range(0, len(r)):
        found = False
        for p in ips:
            if p[0] == r[i][0]:
                ind = ips.index(p)
                ips[ind] = (p[0], p[1]+1)
                found = True
                break
        if not found:
            ips.append((r[i][0], 1))
    ips.sort(key=second_sort, reverse=True)
    tmp = ips[:10]
    # repack
    ips.clear()
    for i in range(0, len(tmp)):
        ips.append(tmp[i][0])
    return ips


def get_top_longs(r):
    longs = []
    for i in range(0, len(r)):
        if i == 0:
            duration = timedelta(0)
        else:
            t1 = r[i][1]
            t0 = r[i-1][1]
            date_0 = datetime.strptime(t0, "%d/%b/%Y:%H:%M:%S")
            date_1 = datetime.strptime(t1, "%d/%b/%Y:%H:%M:%S")
            duration = date_1 - date_0
            if date_0 > date_1:
                duration = date_0 - date_1
                l.warning("time inverse at "+str(i)+" position.")
        longs.append((r[i], duration))
    longs.sort(key=second_sort, reverse=True)
    tmp = longs[:10]
    # repack
    longs.clear()
    for i in range(0, len(tmp)):
        longs.append((tmp[i][0][2], tmp[i][0][3], tmp[i][0][4], tmp[i][0][1]))
    return longs


def get_top_client_errors(r):
    clerr = []
    stat = []
    for i in range(0, len(r)):
        code = r[i][4]
        if 499 < int(code) < 600:
            t = (r[i][0], r[i][2], r[i][3], r[i][4])
            if t in clerr:
                ind = clerr.index(t)
                stat[ind] = stat[ind]+1
            else:
                clerr.append(t)
                stat.append(1)
    tmp=[]
    for i in range(0, len(clerr)):
        tmp.append((clerr[i], stat[i]))
    tmp.sort(key=second_sort, reverse=True)
    tmp = tmp[:10]
    # repack
    clerr.clear()
    for i in range(0, len(tmp)):
        clerr.append((tmp[i][0][1], tmp[i][0][2], tmp[i][0][3], tmp[i][0][0]))
    return clerr


def get_top_server_errors(r):
    srverr = []
    stat = []
    for i in range(0, len(r)):
        code = r[i][4]
        if 399 < int(code) < 500:
            t = (r[i][0], r[i][2], r[i][3], r[i][4])
            if t in srverr:
                ind = srverr.index(t)
                stat[ind] = stat[ind]+1
            else:
                srverr.append(t)
                stat.append(1)
    tmp=[]
    for i in range(0, len(srverr)):
        tmp.append((srverr[i], stat[i]))
    tmp.sort(key=second_sort, reverse=True)
    tmp = tmp[:10]
    # repack
    srverr.clear()
    for i in range(0, len(tmp)):
        srverr.append((tmp[i][0][1], tmp[i][0][2], tmp[i][0][3], tmp[i][0][0]))
    return srverr


# public static void main()
l = Logger("anlogs", "DEBUG")

needle = 'access_log'
a = 'no'
d = './logs'
for opt in sys.argv:
    if opt.startswith('--dir='):
        d = opt[6:]
    if opt.startswith('--all='):
        a = opt[6:]

# is directory exists
if not os.path.isdir(d):
    l.error('directory not exists.')
    sys.exit(-1)

files = []
for f in os.listdir(d):
    if a == 'yes':
        if f.startswith(needle):
            files.append(os.path.join(d, f))
    else:
        if f == needle:
            files.append(os.path.join(d, needle))

#print(files)

# is list empty
if len(files) == 0:
    l.error('log(s) not found.')
    sys.exit(-1)

r = parse_logs(files)
if r[0] > 0:
    l.warning("skipped "+str(r[0])+" rows from logs")

logs = r[1]
total = len(logs)
stat = get_stat_requests(logs)
ips = get_top_ips(logs)
longs = get_top_longs(logs)
client_errs = get_top_client_errors(logs)
server_errs = get_top_server_errors(logs)


out = {}
out['total'] = total
out['stat'] = stat
out['ips'] = ips
out['longs'] = longs
out['client_errs'] = client_errs
out['server_errs'] = server_errs

j = json.dumps(out)

print(j)
