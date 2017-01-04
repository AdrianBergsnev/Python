from netmiko import ConnectHandler

from Device_list import devices

for device in devices:


	conn = ConnectHandler(**device)	

	out = conn.send_command_timing('copy running-config tftp://192.168.0.221/')
	out += conn.send_command_timing("")
	out += conn.send_command_timing("")


	conn.disconnect()
