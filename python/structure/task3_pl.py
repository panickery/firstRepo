#Pg Latin

def pig_latin_translator(word) :
    if word[0:1] in 'aeiou' : 
        print(word+"hay")
    else :
        print(word[1:] + word[0:1] + 'ay')

while True :
    temp = input("Give a word : ")
    if temp == 'done' : 
        pig_latin_translator(temp)
        break
    else :
        pig_latin_translator(temp)
