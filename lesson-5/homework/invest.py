def invest(amount, rate, years):
    for i in range(1,years+1):
        amount *= (1 + rate)
        print(f"year {i}: {round(amount,2)}")

invest(100, 0.05, 4)
