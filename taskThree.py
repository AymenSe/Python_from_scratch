my_list = [*range(1,100)]
this_year = 2019
birthday_year = int(input("Enter the birthday year: "))

your_age = this_year - birthday_year

for age in my_list:
	if age == your_age:
		print(age, "This my age !!")
		break
	print(age, "not my age")
