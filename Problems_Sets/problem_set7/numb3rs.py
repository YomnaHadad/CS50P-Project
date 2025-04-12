import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$" , ip)
    try:
        for group in matches.groups():
            if not (int(group) <= 255):
                return False
        return True
    except:
        return False

if __name__ == "__main__":
    main()
