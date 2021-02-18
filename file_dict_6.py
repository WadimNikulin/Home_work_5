my_dict = {}
with open("textfile_6.txt", 'r', encoding="utf-8") as f:
    for line in f:
        key, val = line.split(":")
        my_str = str()
        for n in val:
            if n.isdigit():
                if n == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
                    my_str += n
            else:
                my_str = my_str + " "
        my_str = my_str.split()
        for el in range(0, len(my_str)):
            my_str[el] = int(my_str[el])  # не понял на что он тут ругается
        sum_val = sum(my_str)
        my_dict[key] = sum_val
    print(my_dict)
