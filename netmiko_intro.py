from netmiko import ConnectHandler


def gather_info(ip_address, provider):
    print(f"###\nConnecting to {ip_address}\n###")
    with ConnectHandler(ip=ip_address, **provider) as device:
        version = device.send_command("show version")
        interfaces = device.send_command("show interfaces")
        #print(version)
        #print(interfaces)
    print(f"###\nDisconnecting from {ip_address}\n###")

def apply_common_config(ip_address, provider):
    common_config = [
        "no ip domain-lookup",
        "ip domain-name alef.lab",
        "no ip arp proxy"
    ]
    print(f"###\nConnecting to {ip_address}\n###")
    with ConnectHandler(ip=ip_address, **provider) as device:
        try:
            result = device.send_config_set(common_config)
            print(result)
        except Exception as e:
            print(f"Failed to configure device {ip_address}. Exception: {repr(e)}")
    print(f"###\nDisconnecting from {ip_address}\n###")
    
def backup_config(ip_address, provider):
   
    print(f"###\nConnecting to {ip_address}\n###")
    with ConnectHandler(ip=ip_address, **provider) as device:
        try:
            config = device.send_command("show run")
            with open(f"{ip_address}.conf", mode="w") as f:
                f.write(config)
        except Exception as e:
            print(f"Failed to configure device {ip_address}. Exception: {repr(e)}")
    print(f"###\nDisconnecting from {ip_address}\n###")

def main():
    provider = {
        "username": "admin",
        "password": "cisco",
        "device_type": "cisco_ios"
    }
    ip_addresses = ["10.8.8.131", "10.8.8.132", "10.8.8.133"]
    for ip_address in ip_addresses:
        # gather_info(ip_address=ip_address, provider=provider)
        # apply_common_config(ip_address=ip_address, provider=provider)
        backup_config(ip_address=ip_address, provider=provider)

if __name__ == '__main__':
    main()