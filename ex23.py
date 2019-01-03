<<<<<<< HEAD
import sys

script, encoding ,error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print(">>>debug ",repr(line),encoding,errors)
        print_line(line, encoding,errors)
        return main(language_file,encoding,errors)
    print("<<<end of main")

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors =errors)

    print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt",encoding = "utf-8")

main(languages,encoding,error)

#pid = int("\u03c0")
##tt = pid.decode('utf-8',errors='strict')
#print(tt)
=======
import sys

script, encoding ,error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print(">>>debug ",repr(line),encoding,errors)
        print_line(line, encoding,errors)
        return main(language_file,encoding,errors)
    print("<<<end of main")

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors =errors)

    print(raw_bytes, "<=====>", cooked_string)

languages = open("languages.txt",encoding = "utf-8")

main(languages,encoding,error)

#pid = int("\u03c0")
##tt = pid.decode('utf-8',errors='strict')
#print(tt)
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
