with open('textfile_2.txt', "r") as f:
    n = 0
    m = 0
    for line in f:
        n += 1
        for word in line.split():
            m += 1
print("Количество срок: " + str(n))
print("Количество слов: " + str(m))