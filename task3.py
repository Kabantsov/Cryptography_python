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

def char_range(start, end, step = 1):
    for char in range(ord(start), ord(end), step):
        yield chr(char)

# работа с текстом после операции xor
def detect_english_text(text):
    # переводим текст в нижний регистр
    lower_text = text.lower()
    str_of_symbols = ''

    # проверяем текст на адекватность
    if all(33 <= ord(char) < 123 or char == ' ' or char == '\n' for char in lower_text):
        str_of_symbols = ''.join(ch for ch in lower_text if
                                 ch.isalpha())  # строка, состоящая только из английских букв без пробелов и лишних символов

    # считаем частоту букв в полученном тексте
    if (len(str_of_symbols) != 0):
        text_freq = {}
        for letter in char_range('a', 'z'):
            text_freq[letter] = round((lower_text.count(letter) / len(str_of_symbols) * 100), 3)

        # считаем вероятность
        i = 0
        probability = 0
        for letter in char_range('a', 'z'):
            probability += round((math.fabs(frequency_english[letter] - text_freq[letter])), 3)
        return (probability)
    else:
        return (-1)


def decrypt(str):
    k = 0
    min_probability = float('inf')
    key = -1
    while (k < 256):  # перебор всевозможных ключей

        # ксорим
        j = 0
        xor_result = []
        symbols = []
        while (j < len(str)):
            dec_char = int(str[j:j + 2:], 16) # ксорим в 10сс
            xor_result.append(dec_char ^ k)
            j += 2

        # результат xor переводим в строку соответствующих символов
        j = 0
        message = ''
        while (j < len(xor_result)):
            symbols.append(chr(xor_result[j]))
            j += 1
        message = ''.join(symbols)

        # успешно ли распознали строку?
        # поиск минимальной вероятности
        answer = detect_english_text(message)
        if (answer == -1):
            k += 1
        else:
            if (min_probability > answer):
                min_probability = answer
                key = k
                text = message
            k += 1

    return key, text


string = '2b4a0605040d4a1e03070f4a0b0d05464a03044a0b4a0d0b060b12134a0c0b18464a0c0b184a0b1d0b1344444444'

result = decrypt(string)
print('Key:', chr(result[0]), '\nDecrypted message:', result[1])


