from netmiko import ConnectHandler

Switch = {
	'device_type': 'cisco_ios',
	'ip': '192.168.xx.xx',
	'username': 'admin',
	'password': 'P@ssw0rd',
}

conn = ConnectHandler(**Switch)

vlan_database = [ 'interface vlan 1', 
				  'ip address 192.168.20.1 255.255.255.0',
				  'interface vlan 10',
				  'interface vlan 20',
				  'interface vlan 30',]				  
				 
configure_interfaces = [ 'interface fastethernet0/1',
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
			 		   'no shut',
			 		   'interface range fastethernet0/23-24',
			 		   'switchport mode trunk',
			 		   'switchport trunk allowed vlan 1,10,20,30',
			 		   'no shut']
			 		  		 		  		
conn.send_config_set(vlan_database)
conn.send_config_set(configure_interfaces)

conn.send_command_expect('write memory')

output = conn.send_command('show run')

conn.disconnect()

print(output)
