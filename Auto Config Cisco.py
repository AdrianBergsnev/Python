from netmiko import ConnectHandler
import os

Switch = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.119',
	'username': 'admin',
	'password': 'Passord123',
}

vlan_database = [
	'interface vlan 1', 
	'ip address 192.168.50.1 255.255.255.0',
	'interface vlan 10',
	'interface vlan 20',
	'interface vlan 30'
]				  
				 
configure_interfaces = [
	'interface fastethernet0/1',
	'switchport mode access',
	'switchport access vlan 1',
	'descripton Admin',
	'no shutdown',
	'interface range fastethernet0/2 - 8',
	'switchport mode access',
	'switchport access vlan 10',
	'descripton Elev',
	'no shutdown',
	'interface range fastethernet0/9 - 14',
	'switchport mode access',
	'switchport access vlan 20',
	'descripton Laerer',
	'no shutdown',
	'interface range fastethernet0/15 - 22',
	'switchport mode access',
	'switchport access vlan 30',
	'descripton Internett',
	'no shutdown',
	'interface range fastethernet0/23-24',
	'switchport mode trunk',
	'switchport trunk allowed vlan 1,10,20,30',
	'no shutdown'
]

wr = 'write memory'
sh_run = 'show running-configuration'
conn = ConnectHandler(**Switch)	
conn.send_config_set(vlan_database)
conn.send_config_set(configure_interfaces)
conn.send_command_expect(wr)

output = conn.send_command(sh_run)

conn.disconnect()

userprofile = os.environ['USERPROFILE']

answer = raw_input('Vil du lagre konfigurasjonen til en tekstfil?[y/n]: ')

if answer == 'y' or answer == 'Y':
	file = open(userprofile + '\\Documents\\Python\\running_config.txt', 'w+')
	file.write(output)
	file.close()

print(output)

'''
Before executing the script:

SSH must be enabled, and username and password must be defined.
