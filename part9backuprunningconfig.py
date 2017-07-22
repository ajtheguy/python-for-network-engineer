##Demonstrate capture telnet input output with 'sh run' 
##for screen scraping running config. 
##Use TFTP to bakcup running config might be better


#!/usr/bin/env python2.7
import getpass
import telnetlib

#Ask for username and password
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

#Open the switches IP address list
f = open('myswitches')

#Telnet to switches and get the running config
for line in f:
    print 'Getting running config from  Switch ' + line
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
      tn.read_until("Password: ")
      tn.write(password + "\n")

    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("terminal length 0\n")
    tn.write("show run\n")

    tn.write("end\n")
    tn.write("exit\n")

    ReadOutput =  tn.read_all()
    SaveOutput = open("switch" + HOST, 'w')
    SaveOutput.write(ReadOutput)
    SaveOutput.close
