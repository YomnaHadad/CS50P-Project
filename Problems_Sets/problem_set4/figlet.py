import sys
from pyfiglet import Figlet
figlet = Figlet()
def main():
    if(check_argv()):
        txt = input("Input: ")
        print(figlet.renderText(txt))
    else:
        sys.exit("invalid")
def check_argv():
    if len(sys.argv) == 1 :
        return True
    else:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
            figlet.setFont(font= sys.argv[2])
            return True
        else:
            return False
main()
