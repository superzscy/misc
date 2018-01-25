#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import httplib
import urllib
import socket
import time

# Use Token, check https://support.dnspod.cn/Kb/showarticle/tsid/227/
ID = replaceme  # relace with yours, get it as link above show you.
Token = replaceme  # relace with yours, get it as above link show you.

params = dict(
    login_token=("%s,%s" % (ID, Token)),
    format="json",
    domain_id=replaceme,  # replace with your domain_od, can get it by API Domain.List
    record_id=replaceme,  # replace with your record_id, can get it by API Record.List
    sub_domain="@",  # replace with your sub_domain
    record_line="默认",  #
)

params2 = dict(
    login_token=("%s,%s" % (ID, Token)),
    format="json",
    domain_id=replaceme,  # replace with your domain_od, can get it by API Domain.List
    record_id=replaceme,  # replace with your record_id, can get it by API Record.List
    sub_domain="www",  # replace with your sub_domain
    record_line="默认",  #
)

current_ip = None


def ddns(ip, domainParams):
    domainParams.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(domainParams), headers)

    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200


def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666), 20)
    ip = sock.recv(16)
    sock.close()
    return ip

if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                if ddns(ip, params) and ddns(ip, params2):
                    current_ip = ip
        except Exception as e:
            print e
            pass
        time.sleep(30)
