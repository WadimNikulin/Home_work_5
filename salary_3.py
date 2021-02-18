salary_min = 20000

with open('textfile_3.txt', "r", encoding='utf-8') as f:
    my_list = []
    for line in f:
        for word in line.split():
            my_list.append(word)

print(my_list)

for n in range(1, len(my_list), 2):
    if int(my_list[n]) < salary_min:
        print("Зарплата меньше 20000: " + my_list[n - 1] + " " + my_list[n])

sum = 0

for n in range(1, len(my_list), 2):
    sum += int(my_list[n])

print("Средняя зарплата:" + str(int(sum / (len(my_list) / 2))))
