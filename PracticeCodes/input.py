print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Tell me anything...") # default is string
print("Hmm...", anything, "...Really?")

anything = float(input("Enter a number: ")) # type casting
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

a=2
print("a="+str(a))

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

a = int(dura / 60)
b = int(dura % 60)
print("End time:",((hour+a)+int((mins+b)/60))%24,":",(mins+b)%60)
