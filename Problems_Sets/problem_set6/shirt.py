import sys
from PIL import Image , ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith('jpg') or sys.argv[1].endswith('png') or sys.argv[1].endswith('jpeg')):
    sys.exit("Invalid output")
elif not (sys.argv[2].endswith('jpg') or sys.argv[2].endswith('png') or sys.argv[2].endswith('jpeg')):
    sys.exit("Invalid output")
elif (sys.argv[1][sys.argv[1].index('.'):] != sys.argv[2][sys.argv[2].index('.'):]):
    sys.exit("Input and output have different extensions")
else:
    try:
        with Image.open(sys.argv[1]) as img , Image.open("shirt.png") as shirt:
            size = shirt.size
            img2 = ImageOps.fit( img , size)
            img2.paste(shirt , shirt)
            img2.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")
