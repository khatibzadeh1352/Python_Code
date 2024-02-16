# Release 02/16/2024   Author  M.KHA1352
import pyfiglet
import colorama
import random
import os,sys,nmap,os.path
import platform
import cryptography
import binascii
import subprocess
import winreg as wrg
import requests
import devcon_win
import hashlib
import ipaddress
global nmap_output_file
global port1
global port2
# for install nmap module pls run pip install python-nmap in terminal
# Begin of input port validation
def input_port_validation() :
        while True:
            try:
                input_port1=input("pls enter your First Port of Port-range:")
            except ValueError:
                print("Error: expect an integer. Try again.")
                continue
            else:
                break
        if input_port1.isdigit()==True:
            if 1 <= int(input_port1) <= 65535:
                print('This is a VALID port number.')
            else:
                print('This is NOT a valid port number.')
        else:
            input_port1="21"
            print('First port range is set to 21.')
        while True:
            try:
                input_port2=input("pls enter your End Port of Port-range:")
            except ValueError:
                print("Error: expect an integer. Try again.")
                continue
            else:
                break
        if input_port2.isdigit()==True:
            if 1 <= int(input_port2) <= 65535:
                print('This is a VALID port number.')
            else:
                print('This is NOT a valid port number.')    
        else:
            input_port2="1000"   
            print('End port range is set to 1000.')    
        return input_port1,input_port2


# End of input_port_validation



# begin of nmap function     
def nmapfunc(target_ip , arg3 ) :
        #ip1=input("pls enter your IP Address/network-range:")
        #port1=input("pls enter your Port/Port-range:")
        # =============== soloution 2
        file1=open(nmap_output_file, 'a')
        nmScan = nmap.PortScanner()
        #nmScan.scan('192.168.113.135', arguments="-sn" )
        nmScan.scan(target_ip, arguments = arg3)
        #print(nmScan.all_hosts()) 
        for host in nmScan.all_hosts():
            print('Host : %s (%s)' % (host, nmScan[host].hostname()))
            file1.write('Host : %s (%s)' % (host, nmScan[host].hostname()))
            file1.write('\n')
            print('State : %s' % nmScan[host].state())
            file1.write('State : %s' % nmScan[host].state())
            file1.write('\n')
            for proto in nmScan[host].all_protocols():
                print('----------')
                file1.write('----------')
                file1.write('\n')
                print('Protocol : %s' % proto)
                file1.write('Protocol : %s' % proto)
                file1.write('\n')
                lport = nmScan[host][proto].keys()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
                    file1.write('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state']))
                    file1.write('\n')
        file1.write("End of This scan")
        file1.close
# End of nmap function

mybanner=pyfiglet.figlet_format("MPK-H@-RI4",font="speed")
print (colorama.Fore.RED+mybanner+colorama.Fore.RESET)
mymenue='''
[1] T0
[2] T1
[3] T2
[4] T3
[5] T4
[6] T5
'''

mymenue2 ='''
[1] WAF Detection(First Approach)
[2] WAF Detection (Second Approach)
[3] Firewall Bypass Scan with Syn Stealth scan for enumeration of access control list
[4] Firewall Bypass Approach with firewall enumaration
[5] Firewall Bypass Approach with tcp windows scanning for firewall enumaration
[6] Firewall Bypass Approach with Custom MTU size 
[7] Firewall Bypas with spoof mac address
[8] Firewall Bypass with with custom data length 
[9] Firewall Bypass with  bad checksum
'''

mymenue3='''
[1] 8
[2] 16
[3] 24
[4] 32
'''

nmap_output_file="nmap1.txt"
flag1="true"
while flag1=="true":
    nmap_output_file=input("pls enter your Scan output file name: ")
    path1 = "./"+nmap_output_file
    check_file = str(os.path.isfile(path1))
    if check_file=="True":
        print("file is exist")
        continue
    else:
        flag1="false"

#mymenue1=["1- Host Discovery","2- UDP Scan","3- SMB Enumeration","4- SYN Scan"]
mymenue1=["1- Host Discovery"+"            "+"9- Silent Scan-SCTP COOKIE ECHO Scan"]
mymenue1.insert(1,"2- UDP Scan"+"                  "+"10- ACK Scan")
mymenue1.insert(2,"3- SMB Enumeration"+"           "+"11- Service Fingerprint")
mymenue1.insert(3,"4- SYN Scan"+"                  "+"12- Fast Scan")
mymenue1.insert(4,"5- NULL Scan"+"                 "+"13- safe script Scan")
mymenue1.insert(5,"6- TCP Scan"+"                  "+"14- Vulnerability Scan (Only run in Linux-Os)")
mymenue1.insert(6,"7- ACK-PING Scan"+"             "+"15- Aggersive Scan")
mymenue1.insert(7,"8- IP Protocol Scan"+"          "+"16- WAF/Firewall Bypass Scan And Detection")
mymenue1.insert(8,"17- Exit"+"          ")
#mymenue1.insert(4,"5- NULL Scan")
#mymenue1.insert(5,"6- TCP Scan")
#mymenue1.insert(6,"7- ACK-PING Scan")
#mymenue1.insert(7,"8- IP Protocol Scan")
#mymenue1.insert(8,"9- Silent Scan-SCTP COOKIE ECHO Scan")
#mymenue1.insert(9,"10- ACK Scan")
#mymenue1.insert(10,"11- Service Fingerprint")
#mymenue1.insert(11,"12- Fast Scan")
#mymenue1.insert(12,"13- safe script Scan")
#mymenue1.insert(13,"14- Vulnerability Scan")
#mymenue1.insert(14,"15- Aggersive Scan")
#mymenue1.insert(15,"16- Exit")
#print(mymenue1)
ip1=""
port1="21"
port2="1000"
port_range=""
arg1=""
delay_chice1=6
delay_choice_input="6"
delay_template="T5"
fragment_status=""
fragment_choice=""
flag2=""
firewall_choice_input="1"
firewall_choice=1
mtu="8"
mtu1=1
data_len="25"
data_len1=25
#print(mymenue1[i])
#print (mymenue)
#print(random.random()
#var1=random.randint(1,3)
#print (var1)
#result = subprocess.run(['devcon', 'hwids', '=usb'],capture_output=True, text=True)

while True : 
    for i in mymenue1 :
        print(i)
    var1 = int(input("please input your choice:"))
    if var1==17: 
        exit()
    elif var1==1:
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue


        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<=0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""
        arg1="-sn "+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)
    
        
    elif var1==2 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue
   
        while True:
            try:
                port1=input("pls enter your First Port of Port-range:")
            except ValueError:
                print("Error: expect an integer. Try again.")
                continue
            else:
                break
        if port1.isdigit()==True:
            if 1 <= int(port1) <= 65535:
                print('This is a VALID port number.')
            else:
                print('This is NOT a valid port number.')
        else:
            port1="21"
            print('First port range is set to 21.')
        while True:
            try:
                port2=input("pls enter your End Port of Port-range:")
            except ValueError:
                print("Error: expect an integer. Try again.")
                continue
            else:
                break
        if port2.isdigit()==True:
            if 1 <= int(port2) <= 65535:
                print('This is a VALID port number.')
            else:
                print('This is NOT a valid port number.')    
        else:
            port2="1000"   
            print('End port range is set to 1000.')     
#        port1=input("pls enter your First Port of Port-range:")
#        port2=input("pls enter your End Port of Port-range:")
        port_range=port1+"-"+port2
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""        
        arg1="-sU -v -p"+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)
    
    elif var1==3 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue


        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""    
        arg1="-v -p 139,445"+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)
    
    elif var1==4 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
    #    port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""        
        arg1="-sS -v -p"+port_range+"-T"+str(delay_chice1)
        nmapfunc(ip1, arg1)
    
    elif var1==5 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1  
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""         
        arg1="-sN -v -p"+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)    
    
    elif var1==6 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2        
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""        
        arg1="-sT -v -p"+port_range+"-T"+str(delay_chice1)
        nmapfunc(ip1, arg1)     
    
    elif var1==7 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2        
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""        
        arg1="-PA -v -p"+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)
    elif var1==8 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1 
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""          
        arg1="-PO -v -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)    
    
    elif var1==9 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""        
        arg1="-sZ -v -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)    
    
    elif var1==10 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1  
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""          
        arg1="-sA -v -P0 -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)   
    
    elif var1==11 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
 #       port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1  
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""              
        arg1="-sV -A --version-light --version-all -v -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)   
        
    elif var1==12 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1    
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""            
        arg1="-sV -F  --version-all -v -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)   
        
    elif var1==13 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
#        port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1   
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""             
        arg1="-sV --version-light --version-all -v --script safe -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)      
       
    elif var1==14 :
        # only possible on kali linux
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue


        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""            
        arg1="-sV --script=vulscan/vulscan.nse "
        nmapfunc(ip1, arg1)  
    
    elif var1==15 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

        port1,port2=input_port_validation()
        port_range=port1+"-"+port2
 #       port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1  
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""              
        arg1="-sV -A -sS -sC -sV --open --reason --version-light --version-all -vv -p "+port_range+"-T"+str(delay_chice1)+fragment_choice
        nmapfunc(ip1, arg1)   
  

    elif var1==16 :
        flag2="true"
        while flag2=="true" :
            ip1=input("pls enter your IP Address/network-range:")
            try:
                ip_object=ipaddress.ip_address(ip1)
                flag2="false"
            except ValueError:
                print("your Ip-Address Syntax Incorrect. pls enter correct IP:")
                continue

    
 #       port1=input("pls enter your Port/Port-range:")
        print(mymenue)
        delay_chice1_input=(input("pls enter your delay template Choice-T0 slower and T5 faster- default is T5: "))
        if delay_chice1_input=="" :
            delay_chice1=6
        else:
            delay_chice1=int(delay_chice1_input)
        if delay_chice1<0 or delay_chice1>6:
            delay_chice1=5
        else:
            delay_chice1=delay_chice1-1  
        fragment_status=input("Do you want fragmentation in scan?y/n: ")
        if fragment_status=="y" or fragment_status=="Y":
            fragment_choice=" -f"
        else:
            fragment_choice=""         

        print(mymenue2)
        firewall_choice_input=(input("pls enter your delay Firewall Choice for Bypass technique- Defauelt is 1: "))
        if firewall_choice_input=="" :
            firewall_choice=1
        else:
            firewall_choice=int(firewall_choice_input)
        if firewall_choice<=0 or firewall_choice>6:
            firewall_choice=1
        if firewall_choice==1:
            arg1=" -p 80,443 --script=http-waf-detect "+"-T"+str(delay_chice1)+fragment_choice
        elif firewall_choice==2:
            arg1=" -p 80,443 --script=http-waf-fingerprint "+"-T"+str(delay_chice1)+fragment_choice
        elif firewall_choice==3:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2        
            arg1="-p "+port_range+" -sS -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice
        elif firewall_choice==4:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2        
            arg1="-p "+port_range+" -sA -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice      
        elif firewall_choice==5:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2        
            arg1="-p "+port_range+" -sW -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice   
        elif firewall_choice==6:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2  
            print(mymenue3)
            mtu=(input("pls enter your MTU Size for Bypass technique- Defauelt is 8: "))
            if mtu=="" :
                mtu1=8 
            elif int(mtu)==2:
                mtu1=16
            elif int(mtu)==3:
                mtu1=24
            elif int(mtu)==4:
                mtu1=32    
            else:
                mtu1=8            
            arg1="-p "+port_range+" -mtu "+str(mtu1)+ " -sA -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice               
            print(arg1)
        elif firewall_choice==7:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2        
            arg1="-p "+port_range+" --spoof-mac 0 -sA -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice     
        elif firewall_choice==8:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2       
            data_len=(input("pls enter your Data_lenght Size for Bypass technique- Defauelt is 25: "))         
            arg1="-p "+port_range+"--data-length "+data_len+ "--spoof-mac 0 -sA -O -PI -PT "+"-T"+str(delay_chice1)+fragment_choice   
        elif firewall_choice==9:
            port1,port2=input_port_validation()
            port_range=port1+"-"+port2        
            arg1="-p "+port_range+" --badsum -sA -O -PI -PT"+"-T "+str(delay_chice1)+fragment_choice
        else:
            arg1=" -p 80,443 --script=http-waf-detect"+"-T "+str(delay_chice1)+fragment_choice                                                
        print(arg1)
        nmapfunc(ip1, arg1)     

                                                                                  
    elif var1 >17 or var1 <1:
         exit()
