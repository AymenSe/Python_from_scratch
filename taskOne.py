choice = input("choose your operation: ")
x = int(input("enter x: "))
y = int(input("enter y: "))
if choice == '+':
	res = x + y
elif choice == '-':
	res = x - y
elif choice == '*':
	res = x * y
elif choice == '%':
	res = x % y
elif choice == '**':
	res = x ** y
elif choice == '//':
	res = x // y
else:
	print("it's not an arithmetic operators")
print(x, choice, y, "=", res)

