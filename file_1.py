with open('textfile_1.txt', "w", encoding='utf-8') as f:
    flag = True
    while flag:
        n = input("Введите текст: ")
        if len(n) != 0:
            f.write(n + '\n')
        else:
            flag = False
