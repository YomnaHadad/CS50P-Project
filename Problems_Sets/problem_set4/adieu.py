import inflect
p = inflect.engine()
l = []
while True:
    try:
        l.append(input("Name: "))
    except EOFError:
        break
print("Adieu, adieu, to " + p.join(l))
