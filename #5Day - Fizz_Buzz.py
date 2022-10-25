f = "Fizz"
b = "Buzz"
fb = "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(fb)
    if number % 3 == 0 and not number % 5 == 0:
        print(f)
    if number % 5 == 0 and not number % 3 == 0:
        print(b)
    else:
        print(number)


