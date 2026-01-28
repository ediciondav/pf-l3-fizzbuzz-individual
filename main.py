for n in range(1, 1001): # Puse 21 para que incluya el número 20
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n) # Es mejor dejarlo en su propia línea por orden