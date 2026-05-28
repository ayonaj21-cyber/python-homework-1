def main():

	print("This program illustrates a chaotic function")

	x = eval(input("Enter a number between 1 and 2: "))
	k = eval(input("Enter a number for our k value "))

	for i in range(30):

		x = k * x * (1 - x)
		print(x)

main()