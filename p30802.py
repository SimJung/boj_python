import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum(map(lambda x: math.ceil(x/T), sizes)))
print(N//P, N%P)