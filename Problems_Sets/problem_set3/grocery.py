l = []  ; D = []  ; result=[]
while True:
    try:
        item = input().lower()
        l.append(item)

    except EOFError:
        for f in l :
            if l.count(f) > 1 and f not in D:
                D.append(f)
        for item in l:
            if item not in D:
                result.append(item)
        result.extend(D)
        for th in sorted(result):
            print(l.count(th) , th.upper())
        break
    
