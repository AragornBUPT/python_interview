import sys

n = 0
prices = []

# time = 2
# for line in sys.stdin:
#     a = line.split()
#     # print(int(a[0]) + int(a[1]))

#     if time == 2:
#         n = int(a[0])
#     elif time == 1:
#         for price in a:
#             prices.append(int(price))
#     else:
#         break

#     time -= 1
n = int(sys.stdin.readline().split()[0])
prices_str = sys.stdin.readline().split()
for price_str in prices_str:
    prices.append(int(price_str))


sum = 0
for i in range(n - 1):
    if prices[i + 1] > prices[i]:
        sum += prices[i + 1] - prices[i]

print(sum)
