#!/usr/bin/env python2.7
import getpass
import sys
import telnetlib

HOST = "192.168.122.72"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")



tn.write("enable\n")
tn.write("cisco\n")

tn.write("conf t\n")

#create vlan 2-20
for n in range (2,21):
 tn.write("vlan " + str( n) + "\n")
 tn.write("name python_vlan_" + str(n) + "\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
