def fibo(n):
    """ 
    A Recursive implementation of the function.
    This implementation is a direct translation of the
    mathematical formula: 
        fibo(0)=0
        fibo(1)=1
        fibo(n)=fibo(n-1)+fibo(n-2)
    """
    if n==0: 
        return 0
    if n==1:
        return 1
    return fibo(n-1) + fibo(n-2)

import timeit

print(timeit.timeit("fibo(15)", "from __main__ import fibo", number=10000))

# First 25 elements in the Fibonacci sequence:
# for val in range(25):
#     print (f"{val} ---> {fibo(val)}")