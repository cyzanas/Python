amount=50
cents=[5,10,25]
print(f"Amount Due: {amount}")
while True:
    coin=int(input("Insert Coin:"))
    if coin in cents:
        amount-=coin
        print(f"Amount Due: {amount}")
    else:
        print(f"Amount Due: {amount}")
        continue

    if amount==0:
        print(f"Change Owed: {amount}")
        break
    elif amount<0:
        amount=abs(amount)
        print(f"Change Owed: {amount}")
        break
    else:
        continue
