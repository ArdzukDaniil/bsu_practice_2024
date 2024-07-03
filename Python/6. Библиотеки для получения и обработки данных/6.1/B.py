import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for line in sys.stdin:
    nums = [int(x) for x in line.split()]
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    print(result)
