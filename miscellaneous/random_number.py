import random

lower = int(input("Enter lower limit for number: "))
upper = int(input("Enter upper limit for number: "))

num = random.randrange(lower, upper + 1)

print("Your random number is " + str(num))
