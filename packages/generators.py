def square_numbers(org_list):
    return [i ** 2 for i in org_list]


def even_sort(org_list):
    return [i for i in org_list if i % 2 == 1]


def str_to_int_sort(org_list):
    return [int(i) for i in org_list if i.isdigit() == True]


def repeat_items(org_list):
    return [i for j in org_list for i in [j, j]]


def primes_gen(num):
    ints_list = [i for i in list(range(2, num + 1))]
    primes_numbers_list = []
    while ints_list:
        prime_number = ints_list.pop(0)
        primes_numbers_list.append(prime_number)
        ints_list = [i for i in ints_list if i % prime_number != 0]
    return primes_numbers_list


def search_div_of_num(num):
    return {num_div for i in range(1, int(num ** 0.5 + 1)) if num % i == 0 for num_div in (i, num // i)}
