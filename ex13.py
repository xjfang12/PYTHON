from sys import argv
#read the WYSS section for how to run this 
script, first, second, third = argv
print (">>>>> argv =", repr(argv))
print ("The script is called: ",script)
print ("The first variable is:",first)
print ("The Second variable is:", second)
print ("The third variable is:", third)