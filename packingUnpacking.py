
data=[4,5,10,23,26,10,57,-9]
print(data)

data.sort()
print(data)
# mini=data[0]
# maxi=data[-1]

mini, *others, maxi=data # "unpacking" mechanism

print(mini, maxi)
print(others)

data=[20,10,30]
first, second, third=data

print(first)

def mysum(*args):
    total=0
    for e in args:
        total += e
    return total

print(mysum(78, 90, 56, 67,89))

data=[4,5,10,23,26,10,57,-9]
print(mysum(*data))
