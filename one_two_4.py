with open('textfile_4.txt', "r", encoding='utf-8') as f:
    my_list = []
    for line in f:
        for word in line.split():
            my_list.append(word)


my_list_1 = ["Один", "Два", "Три", "Четыре"]
my_list_2 = []
m = 0

for n in range(2, len(my_list), 3):
    my_list_3 = []
    my_list_3.append(my_list_1[m])
    my_list_3.append(my_list[n - 1])
    my_list_3.append(my_list[n])
    my_list_2.append(my_list_3)
    m += 1


with open('textfile_4.1.txt', "w", encoding='utf-8') as my_f: # не сообразил как решить
    my_str = str()

    for n in my_list_2:
        my_str = " ".join(n)
        my_f.write(my_str + "\n")
