print("Welcome to tip calculator")
bill=int(input("What is the total bill\n$"))
tip_per=int(input("what percentage tip you want to give 10 12 15:\n%"))
people=int(input("How many people want to split the bill ?\n"))
total=(bill + bill*tip_per/100)/people
final=round(total,2)
print(f"SO the per head cost is {final}""$")


