#Print string statistics

def print_str_statistics(*argv) :
    num_sum = 0
    len_sum = 0
    num_cnt = len(argv)

    for arg in argv :
        num_sum += int(arg)
        len_sum += len(arg)

    print("Average value : ", num_sum/num_cnt)
    print("Total length : ", len_sum)
    print("Average length : ", len_sum/num_cnt)

input_list = []

while True :
    temp = input("Please give a number (0 to exit) : ")

    if int(temp) != 0 :
        input_list.append(temp)
    else :
        print()
        break

print_str_statistics(*tuple(input_list))

# For Test
# print_str_statistics("53", "614", "341", "75", "9454")


