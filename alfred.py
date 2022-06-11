#!/usr/bin/python3
YELLOW = '\033[93m'
GREEN  = '\033[92m'
WHITE  = '\033[0m'
Cyan   = '\033[96m'
RED    = '\033[91m'
print('\033[1m')#<--- For Make Font BOLD 


from os import system , mkdir , popen
import subprocess
import argparse
import socket
import os
import os.path
from os import path
import os,sys
import shutil
import progressbar
from time import sleep


def logo():
    os.system('clear')
    print(WHITE+'''


                ▄▀█ █░░ █▀▀ █▀█ █▀▀ █▀▄
                █▀█ █▄▄ █▀░ █▀▄ ██▄ █▄▀
                   Telegram @SaudTz &  @ip274   


    ''')


logo()

if os.getuid() != 0: # Force to run as sudo
    print("           Please Run As Sudo")
    sys.exit(0)

def tool():
  try:
      # pipe output to /dev/null for silence
      null = open("/dev/null", "w")
      subprocess.Popen("assetfinder", stdout=null, stderr=null)
      null.close()

  except OSError:
      print(YELLOW+"assetfinder not installed please install it first in /usr/bin")
      exit()
  try:
      # pipe output to /dev/null for silence
      null = open("/dev/null", "w")
      subprocess.Popen("subfinder", stdout=null, stderr=null)
      null.close()

  except OSError:
      print(YELLOW+"subfinder not installed please install it first in /usr/bin")
      exit()

  try:
      # pipe output to /dev/null for silence
      null = open("/dev/null", "w")
      subprocess.Popen("httpx", stdout=null, stderr=null)
      null.close()

  except OSError:
      print(YELLOW+"httpx not installed please install it first in /usr/bin")
      exit()
  try:
      # pipe output to /dev/null for silence
      null = open("/dev/null", "w")
      subprocess.Popen("amass", stdout=null, stderr=null)
      null.close()

  except OSError:
      print(YELLOW+"amass not installed please install it first in /usr/bin")
      exit()


def check(domain): # check if target dirctory already exists
    path = domain

    isExist = os.path.exists(path)

    if isExist == False:
        pass

    elif isExist == True:
        try:

            fo = input(RED+"Folder already exists do you wanna delete it?[y,n] "+WHITE)
            if fo == "y" or fo == "Y":
                shutil.rmtree(f"{Domain}")
            elif fo == "n" or fo == "N":
                os.rename(f"{domain}",f"{domain}-OLD")
                
            

            else:
                print("please choose correct option")
                exit()

        except:
            exit()
    else:
        print("something went wrong !")
        exit()

def OneForAll(): # check if OneForAll dirctory exists
    path = "OneForAll"

    isExist = os.path.exists(path)

    if isExist == True:
        pass

    elif isExist == False:
        try:

            fo = input(YELLOW+"OneForAll dirctory not exists do you wanna clone it?[Y,n] "+WHITE)
            if fo == "y" or fo == "Y":
                system(f'git clone https://github.com/shmilylty/OneForAll.git')
                print(YELLOW+"OneForAll has been installed (:"+WHITE)
            elif fo == "n" or fo == "N":
                print(Cyan+"you need to clone 'OneForAll' in the same alfred File"+RED+"  !same letter case!"+WHITE)
                exit()
                           
            else:
                print("please choose correct option")
                exit()

        except:
            exit()
    else:
        print("something went wrong !")
        exit()


def Sublist3r(): # check if tool Sublist3r exists
    path = "Sublist3r"

    isExist = os.path.exists(path)

    if isExist == True:
        pass

    elif isExist == False:
        try:

            fo = input(RED+"Sublist3r dirctory not exists do you wanna clone it?[Y,n] "+WHITE)
            if fo == "y" or fo == "Y":
                system(f'git clone https://github.com/aboul3la/Sublist3r.git')
                print(YELLOW+"Sublist3r has been installed (:"+WHITE)
            elif fo == "n" or fo == "N":
                print(Cyan+"you need to clone 'Sublist3r' in the same alfred File !same letter case!")
                exit()
                           
            else:
                print("please choose correct option")
                exit()

        except:
            exit()
    else:
        print("something went wrong !")
        exit()
Sublist3r()
OneForAll()

def sub(Domain):
    IP_addres = socket.gethostbyname(Domain) # For Get Ip Of Domain
    check(Domain)
    tool()
    mkdir(f"{Domain}")
    



    logo()
    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        |         SubDomains         |  "+WHITE)
    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        Domain:   {}                    ".format(Domain)+WHITE)
    print(Cyan+"        Ip:       {}                    ".format(IP_addres)+WHITE)
    print("\n")



    Hide_output = "> /dev/null 2>&1"

    #Install requirements
    print(GREEN+"[!]Install Requirements For Tools       "+WHITE)
    system(f'pip3 install -r Sublist3r/requirements.txt {Hide_output} && pip3 install -r OneForAll/requirements.txt {Hide_output}')
    print(YELLOW+"[+]Requirements Installed. "+WHITE)
    #Install requirements

    #Get Subdomains From assetfinder
    print(GREEN+"[!]Start Get Subdomains From [assetfinder]       "+WHITE)
    system(f'assetfinder  -subs-only {Domain} > {Domain}/assetfinder.txt')
    print(YELLOW+"[+]SubDomains Have Saved On assetfinder.txt! "+WHITE)
    #Get Subdomains From assetfinder


    #Get Subdomains From subfinder
    print(GREEN+"[!]Start Get Subdomains From [subfinder]       "+WHITE)
    subprocess.check_output(f'subfinder -d {Domain} -silent -o {Domain}/subfinder.txt', shell=True) 
    print(YELLOW+"[+]SubDomains Have Saved On subfinder.txt! "+WHITE)
    #Get Subdomains From subfinder
    

    #Get Subdomains From sublist3r
    print(GREEN+"[!]Start Get Subdomains From [sublist3r]       "+WHITE)
    subprocess.check_output(f'python3 Sublist3r/sublist3r.py -d {Domain} -o {Domain}/sublist3r.txt', shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On sublist3r.txt! "+WHITE)
    #Get Subdomains From sublist3r

    #Get Subdomains From Findomain
    print(GREEN+"[!]Start Get Subdomains From [Findomain]       "+WHITE)
    subprocess.check_output(f'findomain -t {Domain} -o {Domain}/', shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On Findomain.txt! "+WHITE)
    #Get Subdomains From Findomain

    #Get Subdomains From OneForAll
    print(GREEN+"[!]Start Get Subdomains From [OneForAll]       "+WHITE)
    subprocess.check_output(f'python3 OneForAll/oneforall.py --target {Domain} --brute --alive True run --path {Hide_output}', shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On OneForAll File! "+WHITE)
    #Get Subdomains From OneForAll
    
    #Get results From OneForAll
    subprocess.check_output(f'mv OneForAll/results {Domain}/More_results', shell=True)
    #Get results From OneForAll

    #move txt file
    subprocess.check_output(f'mv {Domain}/More_results/temp/*.txt {Domain}', shell=True)
    #move txt file
    
    #Get uniq SubDomains
    subprocess.check_output(f'cut {Domain}/More_results/*.csv -d, -f6  | tail -n +2 | uniq > uniq.txt', shell=True)
    #Get uniq SubDomains

    #Move uniq SubDomains
    subprocess.check_output(f'mv uniq.txt {Domain}/', shell=True)
    #Movw uniq SubDomains

    #Get Subdomains From Amass
    print(GREEN+"[!]Start Get Subdomains From [Amass]       "+WHITE)
    subprocess.check_output(f'amass enum -active -brute -d  {Domain} -o {Domain}/amass.txt {Hide_output}',shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On amass.txt! "+WHITE)
    #Get Subdomains From Amass

    #Get Alive Subdomains From httpx
    print(GREEN+"[!]Start Get Alive Subdomains From [httpx]       "+WHITE)
    subprocess.check_output(f'cat {Domain}/*.txt | httpx -silent -mc 200 -o {Domain}/Sub-Domains200.txt',shell=True)
    print(YELLOW+"[+]Alive SubDomains Have Saved On httpx200.txt! "+WHITE)
    #Get Alive Subdomains From httpx

    #Get Forbidden Subdomains From httpx
    print(GREEN+"[!]Start Get Forbidden Subdomains From [httpx]       "+WHITE)
    subprocess.check_output(f'cat {Domain}/*.txt | httpx -silent -mc 403 -o {Domain}/Sub-Domains403.txt',shell=True)
    print(YELLOW+"[+]Forbidden SubDomains Have Saved On httpx403.txt! "+WHITE)
    #Get Forbidden Subdomains From httpx


    #Filter results
    subprocess.check_output(f'sudo mkdir {Domain}/Tools_results && sudo mkdir {Domain}/Final_results && sudo mv {Domain}/Sub-Domains*.txt {Domain}/Final_results && sudo mv {Domain}/*.txt {Domain}/Tools_results',shell=True)
    #Filter results

    #give access for user
    subprocess.check_output(f'sudo chmod -R ugo+rwx {Domain}',shell=True)
    #give access for user

    print("\n")
    print(GREEN+"-Good News!                                 "+WHITE)
    print(GREEN+"-We Have Get All Subdomains,Happy Hunting.   "+WHITE)
    print("\n")



##########################################
def command():                           #
    try:                                 #                          
        Domain = sys.argv[1]             #  
        return Domain                    #
    except:                              #
        return False                     #
########################################################     
User_Command = command()                               #
                                                       # 
if User_Command == False:                              #
    pass                                               #
else:                                                  #
    Domain = User_Command                              #
    try:                                               #
       sub(Domain)                                     #
    except Exception as ERROR:                         #
        print(RED+"[!]ERROR: {}.".format(ERROR)+WHITE) #
        exit()                                         #
                                                       # 
    exit()                                             #
########################################################

#------- For Nothing -------#
print(Cyan,"Usage: python alfred.py [Domain]")
print(GREEN,'''
    Example:
    python3 alfred.py google.com
''')
exit()
