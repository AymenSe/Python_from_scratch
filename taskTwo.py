
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

for i,m in enumerate(months):
	i += 1
	if i == 2:
		print("This is ", m, " my birthday month!")
		continue
	print(i,m)

