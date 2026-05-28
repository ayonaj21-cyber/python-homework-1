def main():

	print("This program illustrates a chaotic function")

	x = eval(input("Enter a number between 1 and 2: "))
	print("hello")

	for i in range(10):

		x = 3.9 * x * (1 - x)
		print(x)

main()