with open('detectEcb.txt') as file:
    file_lines_list = file.read().splitlines()
file.close()

from binascii import a2b_hex

bin_lines_list = [a2b_hex(x) for x in file_lines_list]  # строки из файла в бинарном представлении

lines_list = []

for i in range(len(bin_lines_list) - 1):
    lines_list.append('')
    for j in range(len(bin_lines_list[i])):
        lines_list[i] += chr(bin_lines_list[i][j])  # формируем символьную строку

for character_string in lines_list:

    list_i_matchings = []  # индексы в строке, с которых начинается искомая подстрока
    for n in range(len(character_string) - 16):
        substring = character_string[n:n + 16:]  # подстрока, которую мы ищем
        found_start_index = str(character_string).find(substring, n + 16)  # первый индекс найденной подстроки
        if found_start_index != -1:
            if len(list_i_matchings) == 0:
                list_i_matchings.append(n)
            list_i_matchings.append(found_start_index)

    if len(list_i_matchings) != 0:

        print('Line: ', str(lines_list.index(character_string)))
        print('Indexes of found blocks:')
        for index in list_i_matchings:
            print('(' + str(index) + ', ' + str(index + 16) + ')')