ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
ans=ans.strip().lower()
l = ["42" , "forty-two" , "forty two"]
if ans in l:
    print("Yes")
else:
    print("No")
