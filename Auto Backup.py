from netmiko import ConnectHandler

from Device_list import devices

#Importing devices from another python script

for device in devices:

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
