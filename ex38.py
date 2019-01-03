<<<<<<< HEAD
from pprint import pprint
ten_things =  "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    pprint(stuff)
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ",stuff)


print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff))
=======
from pprint import pprint
ten_things =  "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    pprint(stuff)
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ",stuff)


print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff))
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
print('#'.join(stuff[3:5]))