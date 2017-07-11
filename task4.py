import task3

def decrypt(str):
    k = 0
    min_probability = float('inf')
    key = -1
    text = ''
    while (k < 256):  # перебор всевозможных ключей

        # ксорим
        j = 0
        xor_result = []
        symbols = []
        while (j < len(str)):
            dec_char = int(str[j:j + 2:], 16)
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
        answer = task3.detect_english_text(message)
        if (answer == -1):
            k += 1
        else:
            if (min_probability > answer):
                min_probability = answer
                key = k
                text = message
            k += 1

    return key, text


file = open('detectSingleXor01')
count = 0
for line in file:
    string = line[0:len(line) - 1:]
    result = decrypt(string)
    count += 1
    if (result[0] != -1):
        print('Number:', count, '\nKey:', result[0], '\nDecrypted message:', result[1])
    else:
        print('Number:', count, '\nNone')
file.close()