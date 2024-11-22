from decimal import Decimal, ROUND_HALF_UP
import sys


def real_round(num):
    return int(Decimal(num).quantize(1, ROUND_HALF_UP))


def read():
    return sys.stdin.readline().rstrip()


n = int(input())

if n == 0:
    print(0)
    exit()

nums = list(map(int, [read() for _ in range(n)]))
nums.sort()

exceptNum = real_round(n * 0.15)
nums = nums[exceptNum:n - exceptNum]
avg = real_round(sum(nums) / len(nums))

print(avg)
