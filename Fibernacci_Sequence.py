# Fibonacci Sequence:

# the result of adding the two numbers that came before it = the new sum in the sequence
# the logic works like this: 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3 ect...
# To automate this in python we CAN structure it like this:


def fib(n):
    a = 0   # a = The first value to be added.
    b = 1   # b = The secound value to be added.
    c = 0   # c = the new value we try to find (will change due to n > c + a).

    if n == 0:
        print(a)            # Line 13 & 14 is put in place to output the value of 0 in the Fibonacci Sequence.
    else:
        print(a)
        print(b)
        while n > c + a:    # 1. If "n" is greater than c + a, since b is the end of the previous calculation c + a should always be lower than "n".
            c = a + b       # 2. since c + a < n we want to tell "c" that a + b = c.
            a = b           # 3. swap/shift value, 0, 1, 1 becomes 1, 1 ect.
            b = c           # 4. swap/shift value. 0, 1, 1 becomes 1, 1 ect.
            print(c)

end_number = int(input())
fib(end_number)
