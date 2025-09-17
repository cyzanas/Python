a=".gif"
b=".jpg"
c=".jpeg"
d=".png"
e=".pdf"
f=".txt"
g=".zip"
ask=input("File Name:").lower()
if a in ask:
    print("image/gif")
elif b in ask:
    print("image/jpeg")
elif c in ask:
    print("image/jpeg")
elif d in ask:
    print("image/png")
elif e in ask:
    print("application/pdf")
elif f in ask:
    print("text/plain")
elif g in ask:
    print("application/zip")
else:
    print("application/octet-stream")
