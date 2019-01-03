<<<<<<< HEAD
i =0
numbers = []


while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def make_list(limit,step):
    test = []
    i =0
    while i < limit:
        print(f"At the top i is {i}")
        test.append(i)

        i = i + step
        print("Test now: ", test)
        print(f"At the bottom i is {i}")
    return test

#a = []
a = make_list(100,2)
=======
i =0
numbers = []


while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def make_list(limit,step):
    test = []
    i =0
    while i < limit:
        print(f"At the top i is {i}")
        test.append(i)

        i = i + step
        print("Test now: ", test)
        print(f"At the bottom i is {i}")
    return test

#a = []
a = make_list(100,2)
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
print("The function return is: " ,a)