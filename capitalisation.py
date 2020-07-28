wealth = int(input("your start capital: "))
add = int(input("Your monthly add: "))
percent = float(input("Input your year percent(in xx.xx format): "))
months = int(input("Input quantity of months: "))

for i in range(months):
	wealth = wealth * (percent/100/12) + wealth + add
	print("Your capitalisation is " + str(wealth * (percent/100/12)))
	print("Your total wealth is " + str(wealth))
	print()