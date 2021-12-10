from netmiko import ConnectHandler

def get_version():
    with ConnectHandler(ip='10.8.8.132', username='admin', password='cisco', device_type='cisco_ios') as device:
        result = device.send_command(command_string='show interfaces', use_textfsm=True)
        print(result)
    

def main():
    get_version()

if __name__ == '__main__':
    main()