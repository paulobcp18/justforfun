print('Up to what number do you want to sum?')

num = int(input())

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))
