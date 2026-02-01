import pyfiglet
import sys
import random

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

font = None

figlet = pyfiglet.Figlet()
fonts = figlet.getFonts()
arg_ind = 1
while arg_ind < len(sys.argv):
    match sys.argv[arg_ind]:
        case "-f"|"--font":
            arg_ind += 1
            font = sys.argv[arg_ind]
            if font not in fonts:
                sys.exit( "Invalid usage")
        case _:
            sys.exit( "Invalid usage")
    arg_ind += 1

if not font:
    font = random.choice(fonts)

#print("font:", font)
figlet.setFont(font=font)
str = input("Input: ")
print("Output:", figlet.renderText(str))
