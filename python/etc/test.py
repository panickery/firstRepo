import re

test = '!m@y# name  is good'
subtext = '+-*/()'

for char in subtext :
    print(re.sub(char, ' ' + char, test))

