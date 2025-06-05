# WrongArgumentError inherit from Exception
# => A WrongArgumentError object is a kind of Exception

class WrongArgumentError(Exception): 
    pass

def isPrime(aNumber):
    """
    isPrime returns True or False depending on the fact that aNumber
    is a prime number or not
    
    Parameters
    ----------
    aNumber : the int to be tested

    Returns
    -------
    True if aNumber is a prime number.
    False if aNumber is not a prime number.
    None if an error is encountered.

    Exception
    --------
    ValueError will be raised if ....
    """
    if not isinstance(aNumber, int):
        ex=ValueError("Wrong type of arg given to isPrime")
        raise ex
    if aNumber <= 1:
        raise WrongArgumentError("Wrong int value provided to isPrime")
    for divisor in range(2,aNumber):
        if aNumber % divisor == 0:
            return False
    return True

nb=int(input("Enter a positive int: "))
result = isPrime(nb)
if result == True:
    print(nb, "is a prime number")
elif result == False:
    print(nb, "is not a prime number")
else:
    print("There is something wrong ...")