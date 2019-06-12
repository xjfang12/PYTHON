from sys import argv
script, filename = argv

txt = open(filename,'r')
print (f"Here's your file {filename}")
print (txt.read())
stringd = "kdkfjalkdjflkaj lkdajkl a"
#txt.write(stringd)
print(txt.read())
txt.close()

print ("Type the filename again:")
file_again = input ("> ")
txt_again = open(file_again,'a')

#print (txt_again.read())
txt_again.write(stringd)
txt_again.close()


print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again, 'r')

print (txt_again.read())
#txt_again.write(stringd)
txt_again.close()
