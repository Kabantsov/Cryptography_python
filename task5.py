
# дублируем ключ до длины исходной строки
def duplicate_key(key, length):
    result = ''
    while (len(result) < length):
        result += key
    if (len(result) != length):
        delta = len(result) - length
        result = result[0:len(result) - delta:]
    return result


#  перевод строки в dec по ascii
def str_to_dec(s):
    symbols = []
    i = 0
    while (i < len(s)):
        symbols.append(ord(s[i]))
        i += 1
    return (symbols)


def xor_repeat_key(str, k):
    symbols_str = str_to_dec(str) # строку переводим в dec по ascii
    key = duplicate_key(k, len(str))
    symbols_key = str_to_dec(key) # ключ переводим в dec по ascii

    xor_result = []
    i = 0
    while (i < len(symbols_str)):
        xor_result.append(hex(symbols_str[i] ^ symbols_key[i]))
        i += 1
    print(xor_result)
    j = 0
    result = ''
    while (j < len(xor_result)): # переводим из hex в string
        h = xor_result[j]
        symbols = h[2:len(h):]
        if ((len(symbols) == 2) or (j == 0)):
            result += symbols
        else:
            result += symbols
        j += 1
    return (result)


string = 'IC'
key = 'ICE'
print(xor_repeat_key(string, key))