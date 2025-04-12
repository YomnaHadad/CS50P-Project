string = input("Input: ")
ans = ""
for char in string:
    if char not in ['A', 'E', 'I', 'O', 'U' , 'a' , 'e' , 'i' , 'o' , 'u']:
        ans += char
print(ans)
