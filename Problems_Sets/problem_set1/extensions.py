s= input("File name: ").strip().lower()
if 'jpg' in s or 'jpeg' in s:
    print("image/jpeg")
elif 'png' in s:
    print("image/png")
elif 'pdf' in s:
    print("application/pdf")
elif 'txt' in s:
    print("text/plain")
elif 'zip' in s:
    print("application/zip")
elif 'gif' in s:
    print("image/gif")
else:
    print("application/octet-stream")
