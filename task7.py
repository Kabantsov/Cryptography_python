from re import sub

# собираем файл в одну строку
with open('decryptAesEcb.txt') as f: # decryptAesEcb.txt
    decrypt_aes_ecb_base64 = sub(r'\n', '', f.read())
f.close()

from binascii import a2b_base64

decrypt_aes_ecb_str = a2b_base64(decrypt_aes_ecb_base64)

with open('encrypted.txt', 'wb') as f1: # файл с аски-представлением
    f1.write(decrypt_aes_ecb_str)
f1.close()

key = b'YELLOW SUBMARINE'
with open('key.txt', 'wb') as f2:
    f2.write(key)
f2.close()

import subprocess
subprocess.call(['openssl', 'enc', '-d', '-aes-128-ecb', '-salt', '-in', 'encrypted.txt', '-out', 'decrypted.txt', '-pass', 'file:key.txt'])
