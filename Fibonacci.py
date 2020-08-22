# Fibon# Fibonacci sequence program
# Note that max integer number is 2147483647 and the sequence will display only 1836311903 as the last number if you ask for 47 or more sequence numbers to be displayed

# definition
def fibo(n):
    a = 0
    b = 1
    if n < 0:
        print("invalid value enter a valid one!")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):  # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a+b
            a = b
            b = c
            if c > 2147483647: # Sequence won't go above million
                break
            print(c)
Check = False
while not Check:
# input command
    try:
        x = int(input("Enter how many Fibonacci sequence numbers you want to display = "))
        Check = True
    except:
        print("That's not a number you dummy!")
# output command
fibo(x)

