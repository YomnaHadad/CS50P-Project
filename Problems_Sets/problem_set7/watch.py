import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.match(r"<iframe.*></iframe>" , s):
        if matches := re.search(r"(https?://(www\.)?youtube\.com/embed/(?P<URL>[a-zA-Z0-9]+))" , s):
            match = matches.group("URL")
            return "https://youtu.be/" + match
if __name__ == "__main__":
    main()
