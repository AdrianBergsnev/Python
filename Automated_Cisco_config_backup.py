from netmiko import ConnectHandler
import netmiko
import json

def get_input(prompt=''):
	try:
		line = raw_input(prompt)
	except NameError:
		line = input(prompt)
	return line

#Prompting

password = get_input('Password: ')

#Defined password prompt for device connection

with open('devices.json') as dev_file:
		devices = json.load(dev_file)

#Importing devices from another .json

for device in devices:

#foreach device in devices, the var contains multiple devices

	device['password'] = password

#Defined password in connection windows before connection to device

	print('Connecting to device', device['ip'])

#Printing the device ip thats being connected

	conn = ConnectHandler(**device)	

#Connecting to the devices imported from .json

	print('Sends TFTP request')
	out = conn.send_command_timing('copy running-config tftp://192.168.0.221/')

#Sending command, and expects a following answer

	out += conn.send_command_timing("")
	out += conn.send_command_timing("")
	print('Config file exported from', device['ip'])

	conn.disconnect()

print('Done!')

#disconnects the SSH session
