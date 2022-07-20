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
#=====///Open Cource
def course():
   
#=====/batas suci(update)
def up():
   os.system('git pull')
#=====/batas suci(about) 
def about():
   os.system('clear')
    print ("              [#] About Informations [#]")
#=====/batas suci(logo)
def logo():
   os.system('clear')
    print("")
    print(cl.end + "           [" + cl.grn + "#" + cl.end + "]" + cl.cyn + " Course Programing " + cl.end + "[" + cl.grn + "#" + cl.end + "]" )
    print()
    print(cl.end + "               Created by " + cl.grn + "Ers ID ")
    print()
#====/batas suci(menu)
def menu():
    print()
    print(" MENU:" )
    print("     1.Open Course")
    print("     2.Update")
    print("     3.About")
    print("     0.Exit")
logo()
menu()
pil=input("[⌨]Chosse: ")
if pil == 1:
   course()
elif pil == 2:
   up()
elif pil == 3:
   about()
elif pil == 0:
   print("Exit program,thanks gan udah mampir ^_^")
   time.sleep(1)
   sys.exit()


#======///done 
