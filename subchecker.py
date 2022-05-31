#!/usr/bin/env python3

import requests
import argparse
import urllib3
import threading
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description="Check if the provided subdomains or URLs are working or not.")
parser.add_argument("-u", "--url", type=str, metavar="",  help="enter the URL (URL should be provided in proper format)")
parser.add_argument("-l", "--list", type=str, metavar="", help="enter the path to file of list of URLs")
args = parser.parse_args()

def req(url):
    if "http://" in url or "https://" in url:
        u = url
        try:
            res = requests.get(u, allow_redirects=False)
            print(str(res.url))
        except: pass    
    else:
        u = "https://" + url
        try:
            res = requests.get(u, allow_redirects=False)
            print(str(res.url))
        except: 
            try:
                u = u.replace("https://", "http://")
                res = requests.get(u, allow_redirects=False)
                print(str(res.url))
            except: pass
    
if args.url: req(args.url)

if args.list:
    list = args.list
    file = open(list, "r")
    
    urls = file.readlines()
    file.close()
    
    for url in urls:
        url = url.replace("\n", "")
        t = threading.Thread(target=req, args=(url,))
        t.start()
