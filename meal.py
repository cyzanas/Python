def main():
    l=convert(input("what time is it : "))
    if l>=7 and l<12:
        print("breakfast time")
    elif l>=12 and l<18:
        print("lunch time")
    elif l>=18:
        print("dinner time")
    else:
        print("go and sleep")

def convert(time):
    hour,minute=time.split(":")
    hour=int(hour)
    minute=int(minute)
    dTime=hour+(minute/60)
    dTime=float(dTime)
    return dTime

if __name__ == "__main__":
    main()
