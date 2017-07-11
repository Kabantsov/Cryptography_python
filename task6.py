import math

frequency_english = {'a': 8.167,
                     'b': 1.492,
                     'c': 2.782,
                     'd': 4.253,
                     'e': 12.702,
                     'f': 2.228,
                     'g': 2.015,
                     'h': 6.094,
                     'i': 6.966,
                     'j': 0.153,
                     'k': 0.772,
                     'l': 4.025,
                     'm': 2.406,
                     'n': 6.749,
                     'o': 7.507,
                     'p': 1.929,
                     'q': 0.095,
                     'r': 5.987,
                     's': 6.327,
                     't': 9.056,
                     'u': 2.758,
                     'v': 0.978,
                     'w': 2.360,
                     'x': 0.150,
                     'y': 1.974,
                     'z': 0.074}


def base64_to_hex(str2):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

    if (len(str2) % 4 != 0):
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

def char_range(start, end, step=1):
    for char in range(ord(start), ord(end), step):
        yield chr(char)

def detect_english_text(text):
    lower_text = text.lower()
    str_of_symbols = ''

    if all(33 <= ord(char) < 123 or char == ' ' or char == '\n' for char in lower_text):
        str_of_symbols = ''.join(ch for ch in lower_text if ch.isalpha())
    if (len(str_of_symbols) != 0):
        text_freq = {}
        for letter in char_range('a', 'z'):
            text_freq[letter] = round((lower_text.count(letter) / len(str_of_symbols) * 100), 3)

        i = 0
        probability = 0
        for letter in char_range('a', 'z'):
            probability += round((math.fabs(frequency_english[letter] - text_freq[letter])), 3)
        return (probability)
    else:
        return (-1)

def decrypt(str):
    res_key = ''
    k = 0
    min_probability = float('inf')
    key = -1
    text = ''
    while (k < 256):

        j = 0
        xor_result = []
        symbols = []
        while (j < len(str)):
            dec_char = int(str[j:j + 2:], 16)
            xor_result.append(dec_char ^ k)
            j += 2

        j = 0
        message = ''
        while (j < len(xor_result)):
            symbols.append(chr(xor_result[j]))
            j += 1
        message = ''.join(symbols)

        answer = detect_english_text(message)
        if (answer == -1):
            k += 1
        else:
            if (min_probability > answer):
                min_probability = answer
                key = k
                text = message
            k += 1
    if (text == ''):
        return ('fail')
    else:
        res_key += (chr(key))
        print(res_key)
        return text

def breaking_xor(file):
    result_words_array = ['' for i in range(41)]  # здесь будет храниться готовый текст

    # соединяем строки из файла в одну большую
    string_file = ''
    for line in file:
        string_file += line[0:len(line) - 1:]

    hex_string_file = base64_to_hex(string_file)

    j = 0
    # words_array = ['' for i in range(41)] # массив длиной 41 из пустых подмассивов, где будут храниться расшифрованные строки
    key_lenght = 2

    while (key_lenght < 41):  # перебираем длину ключа от 2 до 40
        words_array = ['' for i in range(
            key_lenght)]  # массив длиной key_lenght из пустых подмассивов, где будут храниться расшифрованные строки

        i = 0  # номер строки
        while (i < key_lenght):  # перебираем i до значения = key_lenght

            string = ''
            j = i * 2
            while (j < len(hex_string_file)):
                # if (j % key_lenght == i):
                words_array[i] += hex_string_file[j] + hex_string_file[j + 1]
                j += key_lenght * 2

            words_array[i] = decrypt(words_array[i])
            i += 1

        i = 0
        count_fail = 0
        while ((i < len(words_array)) & (count_fail < 1)):
            if (words_array[i] == 'fail'):
                count_fail += 1
            i += 1

        if (count_fail == 0):
            # собираем текст
            count_str = 0
            count_words_array = 0
            count_number_of_line = 0

            while (count_str < len(hex_string_file) / 2):
                count_words_array = count_str % key_lenght
                result_words_array[key_lenght] += words_array[count_words_array][count_number_of_line]
                if (count_words_array == key_lenght - 1):
                    count_number_of_line += 1
                count_str += 1

            print('***********Lenght of the key: ', key_lenght, '\n', result_words_array[key_lenght], '\n')

        else:
            print('***********Lenght of the key: ', key_lenght, '\nfail\n')

        key_lenght += 1

    # for x in result_words_array:
    #    print (x)

    return ('good')


file = open('breakRepeatedKeyXor.txt')
breaking_xor(file)
file.close()