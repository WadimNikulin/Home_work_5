import json
with open('textfile_7.txt', "r", encoding='utf-8') as f:
    my_list_result = []
    my_list_line = []
    for line in f:
        line.split(" ")
        line = line.split()
        my_list_word = []
        for word in line:
            if word.isdigit() == False:
                my_list_word.append(word)
            elif word.isdigit() == True:
                my_list_word.append(int(word))
        my_list_line.append(my_list_word)
    my_dict = {}
    for n in range(0, len(my_list_line)):
        my_dict = {n + 1: my_list_line[n][0], "value": my_list_line[n][2] - my_list_line[n][3]}
        my_list_result.append(my_dict)
    sum_profit = 0
    firm_profit = 0
    for n in range(0, len(my_list_line)):
        if my_list_line[n][2] - my_list_line[n][3] > 0:
            sum_profit += my_list_line[n][2] - my_list_line[n][3]
            firm_profit += 1

    average_profit = sum_profit / firm_profit
    my_dict_average = {"average_profit": average_profit}
    my_list_result.append(my_dict_average)
    print(my_list_result)

with open("my_file.json", "w", encoding='utf-8') as write_f:
    json.dump(my_list_result, write_f)