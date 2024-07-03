def gcd(*args):
    def euclidean_algorithm(a, b):
        while b:
            a, b = b, a % b
        return a

    result = args[0]
    for num in args[1:]:
        result = euclidean_algorithm(result, num)

    return result
