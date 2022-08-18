def prime_numbers(num_range: int) -> None:
    for n in range(1, num_range + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)


print(prime_numbers(10))