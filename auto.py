from subprocess import run, getoutput
from pyfiglet import Figlet
from tabulate import tabulate
from terminaltables import DoubleTable

import os


# if os.geteuid() == 1000:

#     print("Please must be a rooted user :)")
# else:
custom_figlet = Figlet(font="letter")
result = custom_figlet.renderText('Dear Devil')
print(result)

# print(""" \033[1;36m
# ┌═════════════════════════════════════════════════════════════════════════════┐
# █                                                                             █
# █                         Your Network Configuration                          █ 
# █                                                                             █
# └═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m""")
# n_name = os.popen('iwgetid -r').read()  # Get wireless network name
# # Get network mac
# n_mac = os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read()
# n_ipv4 = os.popen("hostname -I | awk '{print$1}'").read()  # Local IP address
# n_ipv6 = os.popen("hostname -I | awk '{print$2}'").read()  # Local IP address
# n_host = os.popen("hostname").read()  # hostname
# gateway_ip = os.popen("ip r | grep default | awk '{print $3}'").read()
# iface = os.popen("ip r | grep default | awk '{print $5}'").read()
# headers = ["IP Address", "MAC Address", "Gateway", "Iface", "Hostname"]
           
# table = [["", "", "", "", ""],
#          ["IPv4 = "+n_ipv4+"IPv6 = "+n_ipv6 , n_mac.upper(), n_name,"Interface Name = "+iface+"Interface IP = "+gateway_ip , n_host]]

# print(tabulate(table, headers, tablefmt="grid"))


# gateway = os.popen("ip r | grep default | awk '{print $3}'").read().replace("\n","")
# scan = os.popen("nmap " + gateway + "/24 -n -sP").read()
# with open('logs/scan.txt',"w") as f:
#     f.write(scan)
# devices = os.popen(" grep report /opt/xerosploit/tools/log/scan.txt | awk '{print $5}'").read()
# devices_mac = os.popen("grep MAC /opt/xerosploit/tools/log/scan.txt | awk '{print $3}'").read() + os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read().upper() # get devices mac and localhost mac address
# devices_name = os.popen("grep MAC /opt/xerosploit/tools/log/scan.txt | awk '{print $4 ,S$5 $6}'").read() + "\033[1;32m(This device)\033[1;m"

			
# table_data = [
# 			    ['IP Address', 'Mac Address', 'Manufacturer'],
# 			    [devices, devices_mac, devices_name]
# 			]
# table = DoubleTable(table_data)
# print(table.table)



