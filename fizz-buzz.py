# For loop to iterate through numbers from 1 to 100 (inclusive)
for i in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        # If divisible by both 3 and 5, print "FizzBuzz"
        print("FizzBuzz")
    # Check if the number is divisible by 3 only
    elif i % 3 == 0:
        # If divisible by 3, print "Fizz"
        print("Fizz")
    # Check if the number is divisible by 5 only
    elif i % 5 == 0:
        # If divisible by 5, print "Buzz"
        print("Buzz")
    # If the number is not divisible by 3 or 5
    else:
        # Print the number itself
        print(i)
        