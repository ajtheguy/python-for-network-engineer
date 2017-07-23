#!/usr/bin/env python2.7

from netmiko import ConnectHandler
import getpass

#Ask for username and password
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': user,
    'password': password,
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': user,
    'password': password,
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': user,
    'password': password,
}


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print "Creating VLAN " + str(n)
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print output 
