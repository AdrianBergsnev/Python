from netmiko import ConnectHandler
import netmiko
import json
import subprocess, sys

with open('devices.json') as dev_file:
		devices = json.load(dev_file)


for device in devices:
	print('Connecting to device', device['ip'])

	conn = ConnectHandler(**device)	

	tftpstring = "copy " + "running-config " + "tftp://192.168.0.90/" + str(device['ip'] + ".txt")

	out = conn.send_command_timing(tftpstring)

	print('Sends TFTP request')

	out += conn.send_command_timing("")
	out += conn.send_command_timing("")

	print('Config file exported from', device['ip'])
	
	conn.disconnect()

## Can be used if you want to export the configs to another location
p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\Admin\\Documents\\PowerShell\Copy-CFGfiles.ps1"], 
              stdout=sys.stdout)
p.communicate()


print('Done!')