months = [ "January" , "February", "March", "April",  "May",
           "June", "July", "August", "September", "October",
           "November", "December" ]
while True:
    try:
        date = input("Date: ").strip()
        if '/' in date:
            m , d , y = date.split('/')
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                print(f"{y}-{int(m):02}-{int(d):02}")
                break
        else:
            m , d ,y = date.split(' ')
            d = int(d[0:len(d)-1])
            if m in months and 1 <= d <= 31:
                print(f"{y}-{(months.index(m) + 1):02}-{d:02}")
                break
    except:
        pass
