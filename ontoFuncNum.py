import math

def calculate_sum(m, n):
    total = 0
    for j in range(n):
        total += math.comb(n, n - j) * ((-1) ** j) * ((n - j) ** m)
    return total

m = 8 # You can change the value of m here
n = 5 # You can change the value of n here

print(calculate_sum(m, n))
