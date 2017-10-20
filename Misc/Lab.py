from netmiko import ConnectHandler

AdrianLAB = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.148',
	'username': 'admin',
	'password': 'Passord123',
}

R1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.146',
	'username': 'admin',
	'password': 'Passord123',
}




conn = ConnectHandler(**AdrianLAB)	

vlan = [
	'interface vlan 300', 'name Elev',
	'interface vlan 500', 'name Servernett'
]

interfaces = [
	'interface range fastethernet0/1 - 10',
	'switchport mode access',
	'switchport access vlan 300',
	'no shutdown',
	'interface range fastethernet0/11 - 13',
	'switchport mode access',
	'switchport access vlan 500',
	'no shutdown',
	'interface range fastethernet0/15-16',
	'switchport mode trunk',
	'switchport trunk allowed vlan 300,500,999',
	'no shutdown'
	'interface range fastethernet0/18'
	'shut'
]

wr = 'write memory'
sh_run = 'sh run'
conn.send_config_set(vlan)
conn.send_config_set(interfaces)
conn.send_command_expect(wr)

output = conn.send_command(sh_run)

conn.disconnect()

print(output)