def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    p=str(d)
    k,l=p.split("$")
    s=l
    s=float(s)
    return s



def percent_to_float(p):
    d=str(p)
    k,l=p.split("%")
    s=k
    s=float(s)
    per=(s/100)
    return per



main()
