"""
this program course free version
created by Ers ID
"""
import os,sys,time 
class cl:
   red="\033[1;31m"
   grn="\033[1;32m"
   ylw="\033[1;33m"
   blu="\033[1;34m"
   pop="\033[1;35m" 
   cyn="\033[1;36m"
   end="\033[0m"
def logo():
   print (cl.end + "[🔰]" + cl.cyn + "Programming Course" + cl.end + "[🔰]")
def menu():
   os.system('clear')
   logo()
   print('')
   print (cl.end + """
      [💻]Menu:
              
               1.Open course
               2.update
               3.about
               4.donate pro version
               0.exit
               
   """)