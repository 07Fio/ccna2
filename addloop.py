import netmiko
from netmiko import ConnectHandler

device_info = {
    "device_type": "cisco_ios",
    "ip": "208.8.8.11",
    "username": "admin",
    "password": "pass",
    "secret": "pass"
}

#Configurations 
script = [
    'interface loopback 0',
    'ip add 1.1.1.1 255.255.255.255',
    'description config-via-py',
    'end'
]



# Push configuration
access_cli = ConnectHandler(**device_info)
output = access_cli.send_config_set(script)

access_cli.disconnect()


print(output)