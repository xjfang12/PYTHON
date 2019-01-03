<<<<<<< HEAD
from sys import argv
script, user_name = argv
prompt = f'{script} ({user_name})> '
print (f"Hi {user_name}, I'm the {script} script.")
print ("I'd like to ask you a few questions.")
print (f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)
print ("What kind of computer do you have?")
computer = input(prompt)

print (f"""
Alright, so you said {likes} about liking me.
Your live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
=======
from sys import argv
script, user_name = argv
prompt = f'{script} ({user_name})> '
print (f"Hi {user_name}, I'm the {script} script.")
print ("I'd like to ask you a few questions.")
print (f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)
print ("What kind of computer do you have?")
computer = input(prompt)

print (f"""
Alright, so you said {likes} about liking me.
Your live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
""")