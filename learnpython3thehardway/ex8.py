formatter = "{} {} {} {}"

print (formatter.format(1,2,3,4))
print (formatter.format("one","two","three","four"))
print (formatter.format(True, False, False, True))
print (formatter.format(formatter,formatter,formatter,formatter))

print (formatter.format("Try your",
                        "Own text here",
                        "Maybe a poem",
                        "Or a song about fear"
                        ), end="\n\n")

print(formatter.format("白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"), end='\n\n')
