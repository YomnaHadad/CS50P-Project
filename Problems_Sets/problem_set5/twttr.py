def main():
    string = input("Input: ")
    print(shorten(string))

def shorten(word):
    ans = ""
    for char in word:
        if char not in ['A', 'E', 'I', 'O', 'U' , 'a' , 'e' , 'i' , 'o' , 'u']:
            ans += char
    return ans

if __name__ == "__main__":
    main()
