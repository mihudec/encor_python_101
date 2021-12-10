
def say_hello(name):
    print(f"Hello {name}")

def main():
    names = ["John", "Alice", "Bob"]
    for name in names:
        if name == "John":
            print("John is blacklisted")
            continue
        say_hello(name=name)
    
    
if __name__ == '__main__':
    main()