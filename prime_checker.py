def prime_checker(number):
    if number < 2:
        print("It's not a prime number")
    else:
        for num in range(2, number):
            if number % num == 0:
                print("It's not prime number")
                break
        else:
            print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number = n)