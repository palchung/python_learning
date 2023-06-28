i = j = sum = 0

while i != -1:
    i = float(input("Please enter a number :"))
    sum += i
    j += 1
    continue

ans = round((sum + 1) / (j - 1), 2)

print("The average of numbers entered =", ans)