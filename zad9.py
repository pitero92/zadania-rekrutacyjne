
def fizzbuzz(n):
    x = range(1,n)
    print(x)


    for i in x:
        if (i % 3 == 0) and (i % 5 == 0):
            print(i)
            print("FizzBuzz")
        elif (i % 3 == 0):
            print(i)
            print("Fizz")
        elif (i % 5 == 0):
            print(i)
            print("Buzz")




print(fizzbuzz(6))
