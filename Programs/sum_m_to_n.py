# Program to find the sum of numbers from m to n.

m = int(input("Enter the starting range: "))
n = int(input("Enter the last range: "))

sum = 0
while (m <= n):
    sum += m
    m += 1

print("The sum of numbers from {0} to {1} is {sum}".format(m,n,sum))