def invest(amount, rate, years):
    amounts=[]
    for i in range(years):
        amount=amount*rate+amount
        print(f"year {i} : {amount:.2f}")
invest(100, 0.05, 4)
