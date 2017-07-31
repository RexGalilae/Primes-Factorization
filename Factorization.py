# List of primes
primes = []
largest = [0]


# Checks if the number is a prime and appends to the list
# if it isn't in it already
def is_prime(num):
    if num in primes:
        return True

    for prime in primes:
        if prime <= num:
            if num % prime == 0:
                return False
        else:
            break

    if not any(num % i == 0 for i in range(2, num)):
        primes.append(num)
        return True


# Ensures that the list contains all primes less than the number
def update_primes(num):
    begin = 2
    if primes != []:
        begin = primes[len(primes) - 1]

    if largest == [] or largest[0] < num:
        for i in range(begin, num):
            if is_prime(i) and i not in primes:
                primes.append(i)
        primes.sort()
        largest[0] = num


def check_prime(num):
    update_primes(num)
    return is_prime(num)


# Returns a list of all factors of the number
def factorize(num):
    prime_factors = []
    check_prime(num)

    test = num
    for prime in primes:
        if prime <= num:
            count = 0
            while test % prime == 0:
                test //= prime
                count += 1
            if count != 0:
                prime_factors.append((prime, count))
        else:
            break

    factors = []
    buffer = []

    # Store the prime factors as a list rather than a list of tuples
    for p in prime_factors:
        for i in range(p[1]):
            buffer.append(p[0])

    # Store the number of combinations of prime factors (with repetition)
    trials = 2 ** len(buffer)

    # For each combination
    for bit in range(trials):
        factor = 1
        # For each element in the list of prime factors
        for i in range(len(buffer)):
            # Include the prime factor in the factor depending on the trial number
            if bit % (2 ** (i + 1)) >= (2 ** i):
                factor *= buffer[i]

        # Append if not present already
        if factor not in factors:
            factors.append(factor)

    # Sort
    factors.sort()
    return prime_factors, factors


# Main Program
while True:
    number = int(input("Enter a positive number : "))
    assert number > 0 and number != 1, "Invalid Input!"
    print()

    print("Check the following options : ")
    print(" [1] : Check if the given number is prime.")
    print(" [2] : Prime factorize the given number.")
    print(" [3] : Factorize the given number.")
    print(" [4] : List all primes till the given number.")
    print(" [X] : Exit Program!")

    print()
    options = input("Enter your desired option(s) : ")
    factorList = []

    if "1" in options:
        if check_prime(number):
            print("{0} is a prime number. {0} is prime #{1}".format(number, primes.index(number) + 1))
        else:
            print("{} is not a prime number.".format(number))

    if "2" in options or "3" in options:
        factorList = factorize(number)
        if "2" in options:
            p_factors = "1"
            for p in factorList[0]:
                for i in range(p[1]):
                    p_factors += " * {}".format(p[0])
            print("\nPrime factorization of {} : {}".format(number, p_factors))

        if "3" in options:
            print("List of factors of {} : ".format(number))
            print(factorList[1])

    if "4" in options:
        print("List of all primes till {} : ".format(number))
        print([prime for prime in primes if prime <= number])

    if "X" in options or "x" in options:
        print("Good Bye!")
        break
    print()