# Reverse pair list

# Differ to using IDE
path = __file__.split('\\')
# print(path)
file_nm = 'words.txt'
path[len(path)-1] = file_nm
file_path = '/'.join(path[2:])

file = open(file_path, 'r')
data = file.read()
list_words = data.split()
# print(list_words)

for i in set(list_words) :
    if i in list_words and i[::-1] in list_words :
        print('{} {}'.format(i, i[::-1]))
        list_words.remove(i)


# TO DELETE :: IDE check, and need to discuss