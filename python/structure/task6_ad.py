# Alice Dictionary
import re

# Differ to using IDE
path = __file__.split('\\')
# print(path)
file_nm = 'alice.txt'
path[len(path)-1] = file_nm
file_path = '/'.join(path[2:])

file = open(file_path, 'r')
data = file.read()
# data = data.replace("\"", " ")
# data = data.replace("\'", " ")
# data = data.replace(")", " ")
# data = data.replace("(", " ")
regex = re.compile('[a-z]([^\s]+)?')
list_words = regex.findall(data)
# list_words = data.split()
print(len(list_words))
word_dict = {}

# for i in list_words[0:10] :
#     print(i)

for i in list_words :
    word_dict[i.lower()] = 0

for i in list_words :
    word_dict[i.lower()] += 1

d_keys = list(word_dict.keys())
d_keys.sort()

for i in d_keys[0:40] :
    print("{}     {}".format(i, word_dict[i]))


# 정규식 사용가능한지, 문자열을 가져올수 있는 라이브러리 사용 가능한지
# 혹시 본문 가지고 있는지(페이지에는 책 내용 말고도 많아서)