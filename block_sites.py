#!/usr/bin/python3
import time
from datetime import datetime
#hosts_path=r'C:\Windows\System32\drivers\etc\hosts'
#hosts_path=r'C:\Games\hosts.txt'
hosts_path='hosts'
redirect='127.0.0.1'
website_list=["www.facebook.com","facebook.com","ok.ru","www.ok.ru","vk.com","www.vk.com"]
start_block_hour=25
end_block_hour=28

def add_block():
    with open(hosts_path,"r+") as f:
        content = f.read()
        for site in website_list:
            if site not in content:
                  print("Adding ",site)
                  f.write(redirect + " " + site + "\n")

def remove_block():
    with open(hosts_path,"r+") as f:
        content=f.readlines()
        removed=False
        for site in website_list:
            if any(site in line for line in content):
                   print("Removing",site)
                   removed=True
                   content.remove(redirect + " " + site + "\n")
        if removed :
           f.seek(0)
           f.writelines(content)
           f.truncate()

while 1:
    now_hour=datetime.now().minute
    print("Now hour: %s. SItes will be locked at %s, unlocked at %s" % (now_hour,start_block_hour,end_block_hour))
    if  ( now_hour >= start_block_hour ) and ( now_hour < end_block_hour):
        print("working time")
        add_block()
    else:
        print("fun time")
        remove_block()
    time.sleep(60)
