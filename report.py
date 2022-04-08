# messenger-reporter

# artin , mmd
#mmd
import os
print()
a = input ("installing libary >> (y/n) ")
if a == "y":
    print()
    os.system("pip install colorama && pip install colored && pip install requests && pip install flags && pip install datetime")
    print()
if a == "n":
    print()
    print ("start wait..")
    
print()
import sys   
import time
import colored                                                  
import colorama                                                 
import datetime
import random
import requests
import flags
import string
import random
import uuid
from colored import fg, bg, attr
from colorama import Fore, Back, Style
time.sleep(1)
os.system("clear")
print(" \n"*10)
print (Fore.GREEN +'')
pl = ["f","¥","€","$","£","¢","&"]
po = ["f","¥","€","$","£","¢","&"]
pi = ["f","¥","€","$","£","¢","&"]
pu = ["f","¥","€","$","£","¢","&","ß","ę","€","$","£","¢","&","₹","₱","†"]
pe = ["ß","ę","€","$","£","¢","&","₹","₱","†"]
pl1 = (random.choice(pl))
pl2 = (random.choice(pl))
pl3 = (random.choice(pl))
pl4 = (random.choice(pl))
pl5 = (random.choice(pi))
pl6 = (random.choice(po))
pl7 = (random.choice(pe))
pl8 = (random.choice(pu))

w = str(datetime.datetime.now())

u = input("Identity you for script code >>> ")
print()
print ()
time.sleep(1)
print(Fore.BLUE + '')


k = (f"""

||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||                             ||||||||||||
||||||||||       ||         ||        ||||||||||||
||||||||||||||                     |||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||
|||  |  |                                |  |  |||
|||  |  |                                |  |  |||
||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||


ʰᵗᵗᵖˢ://ʳᵘᵇⁱᵏᵃ.ⁱʳ/ᶜᵃᵉᵗᵒʳʳ

ᴠᴇʀꜱɪᴏɴ -1.0-  ꜱᴄʀɪᴘᴛ ꜰʀᴇᴇ ᴍᴇꜱꜱᴇɴɢᴇʀꜱ


- {w} -

""")
for n in k:
    sys.stdout.write(n)
    sys.stdout.flush()
    time.sleep(0.009)
#
print()
print()
print (Fore.YELLOW + '')
time.sleep(1)
b = input(f"""

_____________________________
[{u}]>>report 'account' type 
                             
[{u}]>>report 'channel' type 
                             
[{u}]>>report 'group'   type 
                             
[{u}]>>the     'exit'   type 
——————————————————————————————

[{u}]>> ｅｎｔｅｒ tŷpĕ code >> """)
print()
print()
print(Fore.GREEN + '')
print("\r 'loading server'  ..",end="",flush=False) 
time.sleep(1)
print("\r 'loading server'  ...",end="",flush=False)
time.sleep(1) 
print("\r 'loading server'  ....",end="",flush=False) 
time.sleep(1)
print("\r 'loading server'  .....",end="",flush=False) 
time.sleep(1)
print("\r 'loading server'        ",end="",flush=False)
time.sleep(0.8)
print("\r 'loading server'  .",end="",flush=False)
time.sleep(0.9)
print("\r 'loading server'  .. ",end="",flush=False)
time.sleep(0.5)
print("\r 'loading server'  ...",end="",flush=False)
time.sleep(0.7)
print("\r 'loading server'  ....",end="",flush=False)
time.sleep(1)
print("\r 'loading server'  .....",end="",flush=False)
time.sleep(0.7)
print("\r 'create server'           ",end="",flush=False)
time.sleep(0.5)
#
print(Fore.BLUE + '')
if b == "account":
    e = input("username target the create code >> ")
    print ()
    g = requests.get(f"{e}")
    if g.status_code == 200:
        print ()
        print ()
        time.sleep(0.5)
        print (f"account found * '{e}' ")
        print ()
        print ()
    elif g.status_code == 404:
        print ()
        print (f"not found account! '{e}'")
        print ()
    elif c.status_code == 302:
        print ()
        print (f"not found account '{e}' ")
        print ()
    else:
        pass
    time.sleep(0.5)
    f = input (" type code account type 1 or type 2 >> ")
    if f =="1":
        time.sleep(1)
        print ("oked")
        print (Fore.RED + f' [{e}] >> type 1 account code:')
        time.sleep(1)
        print (Fore.GREEN + '')
        print ("____________________")
        print(Fore.BLUE + '')
        q = requests.get("https://raw.githubusercontent.com/FILTERING-RUBIKA-RYSON/for/main/README.md").text
        print(q)
        print(Fore.GREEN)
        print ("____________________")
        print(Fore.YELLOW + '')
        time.sleep(1)
        print (Fore.RED + f" '{u}' 2 order code for <{e}> ")
    if f == "2":
        print ()
        print (Fore.RED +'')
        print()
        time.sleep(1)
        print(f"[{e}]>> type 2 account <code>:")
        print()
        print()
        print (Fore.GREEN +'')
        time.sleep(1)

        print("/______________________/")
        print()
        print(Fore.BLUE + '')
        print (f"((</*<<f<{pl8}<{pl4}<{pl5}<{pl6}<{pl1}<#<=>#>{pl1}>{pl2}>{pl3}>{pl4}>{pl7}>h>>*/>))")
        print ()
        print(Fore.GREEN + '')
        print ("/_____________________/")
        time.sleep(1)
        print()
        print(f" '{u}' 2 order code for <{e}>")

#
if b == "channel":
    print(Fore.BLUE + '')
    y = input("url user target >> donot '@' >>>")
    print(Fore.RED + '')
    c = requests.get(f"{y}")
    if c.status_code == 200:
        print ()
        print ()
        time.sleep(0.5)
        print (f"channel found '{y}' ")
        print ()
        print ()
    elif c.status_code == 404:
        print ()
        print (f"not found channel! '{y}'")
        print ()
    elif c.status_code == 302:
        print ()
        print (f"not found channel! '{y}' ")
        print ()
    else:
        pass
    print()
    print(Fore.RED + '')
    print()
    time.sleep(1)
    print(F"[{y}]>> type channel code: ")
    print()
    print(Fore.GREEN + '')
    time.sleep(0.5)
    print("/________________________/")
    time.sleep(1)
    print(Fore.BLUE + '')
    print(uuid.uuid1())
    print(Fore.GREEN + '')
    time.sleep(0.5)
    print("/________________________/")


if b == "group":
    print(Fore.BLUE + '')
    r = input ("username target for code >> ")
    l = requests.get(f"{r}")
    print(Fore.RED + '')
    if l.status_code == 200:
        print ()
        print ()
        time.sleep(0.5)
        print (f"group found '{r}' ")
        print ()
        print ()
    elif l.status_code == 404:
        print ()
        print (f"not found group! '{r}'")
        print ()
    elif l.status_code == 302:
        print ()
        print (f"not found group '{r}' ")
        print ()
    else:
        pass
    print()
    print(Fore.GREEN + '')
    print()
    print(f" [{r}] >> group code:")
    print(Fore.BLUE + '')
    print("_______________________")
    time.sleep(1)
    print(Fore.RED + '')
    i = requests.get("https://raw.githubusercontent.com/shobadeh/req/main/README.md").text
    print (i)
    print(Fore.BLUE +'')
    print("_______________________")
    print()
    print(Fore.YELLOW +'')
    print(f" '{u}'>> 2 order code for <{r}>")
    print()
    print()
    
#    
    
time.sleep(3)
print(Fore.GREEN +'')
print("messengers reporter script")
print()
print()
print(Fore.WHITE +'')
me = input("restart -1- | exit -2- >>> _ ")
print()
print
if me == "1":
    os.system("python report.py")
    
if me == "2":
    sys.exit
    os.system("exit")

if b == "exit":
    sys.exit

#   
