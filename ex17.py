<<<<<<< HEAD
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying from {from_file} to {to_file}")

#we could do these two on line, how?

in_file = open(from_file,encoding='utf-8')
print (f"The in_file is",repr(in_file))
indata = in_file.read()
print (f"The input file is {len(indata)} bytes long.")
print (f"Does the output file exists? {exists(to_file)}")

print (f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w',encoding='utf-8')
out_file.write(indata)
print ("Alright, all done.")
out_file.close()
in_file.close()
=======
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying from {from_file} to {to_file}")

#we could do these two on line, how?

in_file = open(from_file,encoding='utf-8')
print (f"The in_file is",repr(in_file))
indata = in_file.read()
print (f"The input file is {len(indata)} bytes long.")
print (f"Does the output file exists? {exists(to_file)}")

print (f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w',encoding='utf-8')
out_file.write(indata)
print ("Alright, all done.")
out_file.close()
in_file.close()
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
