from netmiko import ConnectHandler

'''
from Device_list import devices
'''
import netmiko
import json


def get_input(prompt=''):
	try:
		line = raw_input(prompt)
	except NameError:
		line = input(prompt)
	return line

password = get_input('Password: ')


with open('devices.json') as dev_file:
		devices = json.load(dev_file)

#Importing devices from another python script

for device in devices:

	device['password'] = password

#foreach device in devices, the var contains multiple devices

	conn = ConnectHandler(**device)	

#Connecting to the devices thats in the var

	out = conn.send_command_timing('copy running-config tftp://192.168.0.221/')

#Sending command, and expects a following answer

	out += conn.send_command_timing("")
	out += conn.send_command_timing("")

#Sends the "Enter" keystroke to the commandline

	conn.disconnect()

#disconnects the SSH session
