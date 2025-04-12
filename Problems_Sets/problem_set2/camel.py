def main():
    name = snake(input("camelCase: "))
    print("snake_case:" , name)

def snake(name):
    temp = ""
    for char in name :
        if char.islower():
            temp += char
        else:
            temp += '_' + char.lower()
    return temp
main()
