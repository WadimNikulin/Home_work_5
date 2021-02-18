import random
with open('textfile_5.txt', "w", encoding="utf-8") as f:
    for n in range(0, 10):
        a = random.randint(0, 10)
        a = str(a)
        f.write(a + " ")

with open('textfile_5.txt', "r", encoding="utf-8") as f:
    my_list = []
    for line in f:
        for word in line.split():
            my_list.append(int(word))
print(my_list)
print(sum(my_list))