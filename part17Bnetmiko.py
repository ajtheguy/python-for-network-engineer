#!/usr/bin/env python2.7

from netmiko import ConnectHandler
import getpass

#Ask for username and password
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': user,
    'password': password,
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': user,
    'password': password,
}

# iosv_l2_s3 = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.122.73',
#     'username': user,
#     'password': password,
# }

# iosv_l2_s4 = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.122.74',
#     'username': user,
#     'password': password,
# }

# iosv_l2_s5 = {
#     'device_type': 'cisco_ios',
#     'ip': '192.168.122.75',
#     'username': user,
#     'password': password,
# }


with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print lines


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output 

# with open('iosv_l2_access') as f:
#     lines = f.read().splitlines()
# print lines

# # with open('iosv_l2_cisco_design') as f1:
# #     lines1 = f1.read().splitlines()
# # print lines1

# all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

# for devices in all_devices:
#     net_connect = ConnectHandler(**devices)
#     output = net_connect.send_config_set(lines)
#     # output1 = net_connect.send_config_set(lines1)
#     print output 
#     # print output1
 


