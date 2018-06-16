import time
from datetime import datetime
#hosts_path=r'C:\Windows\System32\drivers\etc\hosts'
hosts_path=r'C:\Games\hosts.txt'
redirect='127.0.0.1'
website_list=["www.facebook.com","facebook.com","ok.ru","www.ok.ru","vk.com","www.vk.com"]
start_block_hour=10
end_block_hour=17

def remove_line(record):
    new_content=[]
    with open(hosts_path,"r") as fr:
        for line in fr.readlines():
            if line != record:
                new_content.append(line)
    with open(hosts_path,"w") as fw:
        fw.writelines(new_content)

def add_block():
    print("Adding block")
    with open(hosts_path,"a") as f:
        for site in website_list:
            f.write(redirect + " " + site + "\n")

def remove_block():
    print("Removing block")
    for site in website_list:
       remove_line(redirect + " " + site + "\n")

while 1:
    now_hour=datetime.now().hour
    if  ( now_hour >= start_block_hour ) and ( now_hour < end_block_hour):
        add_block()
        while now_hour < end_block_hour:
            now_hour=datetime.now().hour
            print("Now hour: %s. Waiting for %s to stop blocking" % (now_hour,end_block_hour))
            time.sleep(60)
        remove_block()
    print("Now hour: %s. Waiting for %s to start blocking" % (now_hour,start_block_hour))
    time.sleep(60)
