import re

alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')


def hex_to_base64(str):
    if (len(str) % 2 != 0):
        return ('fail')
    else:
        bin_string = bin(int(str, 16))  # переводим hex-string в bin-string
        while (len(str) * 4 != len(bin_string) - 2):  # проверка, чтобы двоичное представление было "полноценным"
            bin_string += '0'

        count = 0  # считаем, сколько добавляем нулевых байтов
        while ((len(bin_string) - 2) % 3 != 0):
            bin_string += '00000000'
            count += 1

        i = 2
        result = ''
        while (i < len(bin_string)):
            block = bin_string[i:i + 6:]  # из двоичного представления строки берём блоки по 6 символов
            decimal_of_block = int(block, 2)  # получаем десятичное представление блока
            result += alphabet[
                decimal_of_block]  # записываем символ по таблице Base64, соответствующий номеру с предыдущего шага
            i += 6  # переходим к следующему блоку

        if (count == 0):  # проверяем, были ли добавлены нулевые байты
            return (result)
        else:
            j = len(result) - count
            check_list = list(result)
            while (j < len(result)):
                check_list[j] = '='
                j += 1
            result = ''
            result = ''.join(check_list)
            return (result)


def base64_to_hex(str2):
    if (len(str2) % 4 != 0):
        return ('fail')

    p = re.compile('\\=')
    l = len(p.findall(str2))

    if (l > 2):
        return ('fail')

    for k in range(l):
        if str2[-1 - k] != '=':
            return ('fail')

    else:
        i = 0
        k = 0
        bin_result = ''
        while (i < len(str2)):
            if (str2[i] == '='):
                bin_result += '000000'
                k += 1
            else:
                j = 0
                while (str2[i] != alphabet[j]):
                    j += 1
                bin_str = ''
                bin_str += bin(int(str(j), 10))
                if ((len(bin_str) - 2) != 6):
                    n = 6 - (len(bin_str) - 2)
                    l = 0
                    temp = ''
                    while (l < n):
                        temp += '0'
                        l += 1
                    temp += bin_str[2:8:]
                    bin_str = ''
                    bin_str = temp
                    bin_result += bin_str
                else:
                    bin_result += bin_str[2:8:]
            i += 1

        if (k != 0):
            temp = ''
            temp = bin_result[0:len(bin_result) - k * 8:]
            bin_result = ''
            bin_result = temp
        i = 0
        hex_string = ''
        while (i < len(bin_result)):
            temp = ''
            temp = bin_result[i:i + 4:]
            h = hex(int(temp, 2))
            hex_string += h[2:4:]
            i += 4
        return (hex_string)


hex_string = 'faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0'
decode_string = 'A==='

print(hex_to_base64(hex_string))
print(base64_to_hex(decode_string))
