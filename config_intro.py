def generate_interface_config(name, description=None):
    if description is None:
        config = f"interface {name}\n "
    else:
        config = f"interface {name}\n description {description}\n!"
    return config

def main():
    interfaces = [
        {"name": "Vlan10", "description": "Management Interface"},
        {"name": "Vlan20", "description": "VoIP"},
        {"name": "Vlan30", "description": None}
        ]
    # Print indices until 2
    # print(interfaces[:2])
    # Print indices from 1
    # print(interfaces[1:])
    # Print value of key 'description' in the last interface dictionary
    # print(interfaces[-1]['description'])
    
    for interface in interfaces:
        config_string = generate_interface_config(
            name=interface['name'], 
            description=interface['description']
        )
        print(config_string)
    

if __name__ == '__main__':
    main()