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


def logo():
    print(WHITE+'''


                ▄▀█ █░░ █▀▀ █▀█ █▀▀ █▀▄
                █▀█ █▄▄ █▀░ █▀▄ ██▄ █▄▀
                    @SaudTz &  @ip274   


    '''+RED)


logo()



def sub(Domain):
    IP_addres = socket.gethostbyname(Domain) # For Get Ip Of Domain
    mkdir(f"{Domain}")

    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        |         SubDomains         |  "+WHITE)
    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        Domain:   {}                    ".format(Domain)+WHITE)
    print(Cyan+"        Ip:       {}                    ".format(IP_addres)+WHITE)
    print("\n")

    #Install requirements
    print(GREEN+"[!]Install Requirements For Tools       "+WHITE)
    system(f'pip3 install -r Tools/Sublist3r/requirements.txt && pip3 install -r Tools/OneForAll/requirements.txt')
    print(YELLOW+"[+]Requirements Installed. "+WHITE)
    #Install requirements

    #Get Subdomains From assetfinder
    print(GREEN+"[!]Start Get Subdomains From [assetfinder]       "+WHITE)
    system(f'assetfinder  -subs-only {Domain} > {Domain}/assetfinder.txt')
    print(YELLOW+"[+]SubDomains Have Saved On assetfinder.txt! "+WHITE)
    #Get Subdomains From assetfinder


    #Get Subdomains From subfinder
    print(GREEN+"[!]Start Get Subdomains From [subfinder]       "+WHITE)
    subprocess.check_output(f'subfinder -d {Domain} -o {Domain}/subfinder.txt', shell=True) 
    print(YELLOW+"[+]SubDomains Have Saved On subfinder.txt! "+WHITE)
    #Get Subdomains From subfinder
    

    #Get Subdomains From sublist3r
    print(GREEN+"[!]Start Get Subdomains From [sublist3r]       "+WHITE)
    subprocess.check_output(f'python3 Tools/Sublist3r/sublist3r.py -d {Domain} -o {Domain}/sublist3r.txt', shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On sublist3r.txt! "+WHITE)
    #Get Subdomains From sublist3r

    #Get Subdomains From OneForAll
    print(GREEN+"[!]Start Get Subdomains From [OneForAll]       "+WHITE)
    subprocess.check_output(f'python3 Tools/OneForAll/oneforall.py --target {Domain} --brute --alive True --takeover True run --path', shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On OneForAll File! "+WHITE)
    #Get Subdomains From OneForAll
    
    #Get results From OneForAll
    print(GREEN+"[!] Get Results From [OneForAll]       "+WHITE)
    subprocess.check_output(f'mv Tools/OneForAll/results /{Domain}/OneForAll', shell=True)
    print(YELLOW+"[+]Results Have been Moved To Target File! "+WHITE)
    #Get results From OneForAll

    #move txt file
    print(GREEN+"[!]Gather text Files From [OneForAll]       "+WHITE)
    subprocess.check_output(f'mv {Domain}/OneForAll/temp/*.txt /{Domain}', shell=True)
    print(YELLOW+"[+]text Files Have been Moved Into Target File! "+WHITE)
    #move txt file

    #Get Subdomains From Amass
    print(GREEN+"[!]Start Get Subdomains From [Amass]       "+WHITE)
    subprocess.check_output(f'amass enum -active -brute -d  {Domain} -o {Domain}/amass.txt',shell=True)
    print(YELLOW+"[+]SubDomains Have Saved On amass.txt! "+WHITE)
    #Get Subdomains From Amass

    #Get Alive Subdomains From httpx
    print(GREEN+"[!]Start Get Alive Subdomains From [httpx]       "+WHITE)
    subprocess.check_output(f'cat {Domain}/*.txt | httpx -mc 200 -o {Domain}/httpx200.txt',shell=True)
    print(YELLOW+"[+]Alive SubDomains Have Saved On httpx200.txt! "+WHITE)
    #Get Alive Subdomains From httpx

    #Get Forbidden Subdomains From httpx
    print(GREEN+"[!]Start Get Forbidden Subdomains From [httpx]       "+WHITE)
    subprocess.check_output(f'cat {Domain}/*.txt | httpx -mc 403 -o {Domain}/httpx403.txt',shell=True)
    print(YELLOW+"[+]Forbidden SubDomains Have Saved On httpx403.txt! "+WHITE)
    #Get Forbidden Subdomains From httpx

    print("\n")
    print(GREEN+"-Good News!                                 "+WHITE)
    print(GREEN+"-We Have Get All Subdomains,Happy Hunting.   "+WHITE)
    print("\n")



def scan(Domain):
    IP_addres = socket.gethostbyname(Domain) # For Get Ip Of Domain

    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        |          Scan Nmap         |  "+WHITE)
    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        Domain:   {}                    ".format(Domain)+WHITE)
    print(Cyan+"        Ip:       {}                    ".format(IP_addres)+WHITE)
    print("\n")


    #nmap Scan
    print(GREEN+"[!]Start nmap Scan"+WHITE)
    print("\n")
    system('sudo nmap -sV -Pn {}'.format(Domain))
    #nmap Scan

    print("\n")

    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        |          Scan Nikto        |  "+WHITE)
    print(Cyan+"        ------------------------------  "+WHITE)
    print(Cyan+"        Domain:   {}                    ".format(Domain)+WHITE)
    print(Cyan+"        Ip:       {}                    ".format(IP_addres)+WHITE)
    print("\n")

    #Nikto Scan
    print(GREEN+"[!]Start Nikto Scan"+WHITE)
    print("\n")
    system('nikto -h {}'.format(Domain))
    #Nikto Scan


    print("\n")




#-----------------From Here I Get User Input-----------------#
argument = argparse.ArgumentParser(add_help=False)           #
                                                             #
argument.add_argument("-h","--help","-help",action='store_true')     #
                                                             #
argument.add_argument("-sub","--sub")                        #
argument.add_argument("-scan","--scan")                      #
                                                             #  
option = argument.parse_args()                               #
#-----------------From Here I Get User Input-----------------#


#-----------------If User Ask For Help!-----------------#
if option.help:                                         #
    print(f'''{Cyan}    
Usage: python alfred.py [option]                          
Options:
   -sub , --sub       To get SubDomains That The Domain provide.
   -scan, --scan      To Get information on the services and operating systems they are running By This Domain''')
    print(GREEN,'''
    Example:
    python3 alfred.py -sub google.com
    python3 alfred.py -scan google.com
''')
    exit()                                              #
#-----------------If User Ask For Help!-----------------#

if option.sub:
    Domain = option.sub
    try:
       sub(Domain)
    except Exception as ERROR:
        print(RED+"[!]ERROR: {}.".format(ERROR)+WHITE)
        print(RED+"Error Code: 147"+WHITE)

        exit()

    exit()

if option.scan:
    Domain = option.scan
    try:
        scan(Domain)
    except Exception as ERROR:
        print(RED+"[!]ERROR: {}.".format(ERROR)+WHITE)
        print(RED+"Error Code: 159"+WHITE)

        exit()  

    exit()



#------- For Nothing -------#
print(Cyan,'''    
Usage: python alfred.py [option]                          
Options:
   -sub , --sub       To get SubDomains That The Domain provide.
   -scan, --scan      To Get information on the services & ports and operating systems they are running By This Domain ''')
print(GREEN,'''
    Example:
    python3 alfred.py -sub google.com
    python3 alfred.py -scan google.com
''')
exit()