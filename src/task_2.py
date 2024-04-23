from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
from task_1 import cbcEncryption

key = get_random_bytes(16)
iv = get_random_bytes(16)


def submit(userInput):
    urlString = 'userid=456;userdata=' + userInput + ';session-id=31337'
    plaintext = urlString.replace(';', '%3B').replace('=', '%3D')
    return cbcEncryption(key, iv, plaintext)


def verify(cipherText):
    cipherAES = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipherAES.decrypt(cipherText), AES.block_size)
    urlString = plaintext.decode("latin-1")

    if (urlString.__contains__(";admin=true;")):
        print(urlString)
        return True
    else:
        print(urlString)
        return False


if __name__ == "__main__":
    userInputs = input("Type Something: ")

    cipherText = submit(userInputs)

    print(f'Before attack: {verify(cipherText)}')

    cipherNewText = bytearray(cipherText)
    URLString = ('userid=456;userdata=' + userInputs
                 + ';session-id=31337').replace(';', '%3B').replace('=', '%3D')

    attack = ';admin=true;'

    for i in range(len(attack)):
        cipherNewText[i] = cipherNewText[i] ^ ord(URLString[16 + i]) ^ ord(attack[i])

    print(f'After attack: {verify(cipherNewText)}')