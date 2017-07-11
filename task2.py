
def xor(str1, str2):
    if (len(str1) != len(str2)):
        return ("Arrays do not match!")
    else:
        i = 0
        xor_result = []
        while (i < len(str1)):
            dec_str1 = int(str1[i:i + 2:], 16)  # hex to dec
            dec_str2 = int(str2[i:i + 2:], 16)
            xor_result.append(hex(dec_str1 ^ dec_str2))
            i += 2

        j = 0
        result = ''
        while (j < len(xor_result)): # hex переводим в string
            h = xor_result[j]
            symbols = h[2:len(h):]
            if (len(symbols) == 2):
                result += symbols
            else:
                result += '0'
                result += symbols
            j += 1
        return (result)


st1 = '8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69'
st2 = 'bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166'

print(xor(st1, st2))