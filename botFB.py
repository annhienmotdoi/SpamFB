try:
  import os
  import threading
  import subprocess
  import keyboard
  import time
  from colorama import Fore, Style,init
  from pathlib import Path
  from os import path
except ModuleNotFoundError:
        subprocess.call("pip3 install keyboard", shell=True)
        subprocess.call("pip3 install colorama", shell=True)
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor

ban = """\033[1;31m

\033[1;35m Connected To Server...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ☆ ·.¸(`’·.¸*¤*¸.·’´)¸.·
».·º`·.LOVE.·´º·.«
☆.·'(¸.·’´*¤*`’·.¸)`’·.

、、、、、、

☆·.¸(`’·.¸*¤*¸.·’´)¸.·
».·º`·. YOU.·´º·.«
☆.·'(¸.·’´*¤*`’·.¸)`’·.

、、、、、、

☆·.¸(`’·.¸*¤*¸.·’´)¸.·
».·º`· .FOR.·´º·.«
☆.·'(¸.·’´*¤*`’·.¸)`’·.

、、、、、、

☆·.¸(`’·.¸*¤*¸.·’´)¸.·
».·º`· .EVER.·´º·.«
☆.·'(¸.·’´*¤*`’·.¸)`’·.

、、、、、、

。ーゞ丷 My |0Ｖ3
☆。ღHAPPYღ。☆


\033[1;35m 
\033[1;37m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Copyright © by An_nhien_mot_doi software (AT)
\033[1;91m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

\033[1;32m Contact Zalo: AT
\033[1;31m Contact FB : facebook.com/tn.at.169
\033[1;35m Donate MOMO app: 0349829457
\033[1;37m Share with Copyright 
\033[1;35m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Attention:
  * Are you sure ?
  * This may have legal implications.
  * Make sure you're not drunk !
\033[1;31m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
def banner():
  os.system("clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.0003)   
banner()


class spam :
    def checkfile(self) :
        if path.exists('spam.txt'):
           ask = input(str("File already Present\nDo you want to over write(yes or no) : "))
           if "yes" in ask :
                self.write()      
                self.spams()
           else :
             self.spams()
        else :
         self.write()
               
      
    def write(self) :
      f = open('spam.txt', 'w')
      s = int(input("Enter the number of line you want to write : "))
      for i in range(s) :
        n =input(str("Enter the characters you want to write : "))
         
        f.write(n)
        f.write("\n")
    
       

    def spams(self):
        print("Now Place the cursor where you want to spam")
        time.sleep(6)
        while True:
        
           file=open("spam.txt", 'r')
           x=file.read()
           keyboard.write(x)
           time.sleep(3)
           keyboard.send("enter")
    def main(self) :
           self.checkfile()
           self.spams()           
x = spam()  
x.main()       





class spam :
    def checkfile(self) :
        if path.exists('spam.txt'):
           ask = input(str("File already Present\nDo you want to over write(yes or no) : "))
           if "yes" in ask :
                self.write()      
                self.spams()
           else :
             self.spams()
        else :
         self.write()
               
      
    def write(self) :
      f = open('spam.txt', 'w')
      s = int(input("Enter the number of line you want to write : "))
      for i in range(s) :
        n =input(str("Enter the characters you want to write : "))
         
        f.write(n)
        f.write("\n")
    
       

    def spams(self):
        print("Now Place the cursor where you want to spam")
        time.sleep(6)
        while True:
        
           file=open("spam.txt", 'r')
           x=file.read()
           keyboard.write(x)
           time.sleep(3)
           keyboard.send("enter")
    def main(self) :
           self.checkfile()
           self.spams()           
x = spam()  
x.main()       
