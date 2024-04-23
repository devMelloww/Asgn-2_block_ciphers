from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Generating a random key
def generateKey():
    return get_random_bytes(16)


# Generating a random IV
def generateIV():
    return get_random_bytes(16)


# PKCS#7 padding
def pkcs7Padding(data):
    paddingLength = AES.block_size - len(data) % AES.block_size
    padding = bytes([paddingLength]) * paddingLength
    return data + padding


# ECB encryption
def ecbEncryption(key, plainText):
    cipher = AES.new(key, AES.MODE_ECB)
    text = pkcs7Padding(plainText)
    encryptedText = b''
    for i in range(0, len(text), 16):
        block = text[i:i + 16]
        encryptedText += cipher.encrypt(block)
    return encryptedText


# CBC encryption
def cbcEncryption(key, iv, plainText):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b""
    prev_block = iv
    for i in range(0, len(plainText), AES.block_size):
        block = plainText[i:i + AES.block_size]
        if len(block) < AES.block_size:
            block = pkcs7Padding(block)
        block = bytes([a ^ b for a, b in zip(block, prev_block)])
        encrypted_block = cipher.encrypt(block)
        ciphertext += encrypted_block
        prev_block = encrypted_block
    return ciphertext


def encrypt_bmp(imgPath, Encryption, key, IV):
    with open(imgPath, "rb") as file:
        plaintext = file.read()
        header = plaintext[:54]
        plaintext = plaintext[54:]

    if Encryption == "ECB":
        encrypted_data = ecbEncryption(key, pkcs7Padding(plaintext))
    elif Encryption == "CBC":
        encrypted_data = cbcEncryption(key, IV, pkcs7Padding(plaintext))

    return header, encrypted_data


def save_encrypted_bmp(header, ecb_encrypted, cbc_encrypted, Encryption):
    encrypted_img_path = f"C:/Users/shivp/Desktop/CSC321/Asgn-2/resources/encryptedData/{Encryption.lower()}.bmp"
    with open(encrypted_img_path, "wb") as file:
        file.write(header + ecb_encrypted)
        file.write(header + cbc_encrypted)

    print(f"Encrypted message created at: {encrypted_img_path}")


if __name__ == '__main__':
    # Generating random key and IV
    secret_key = generateKey()
    IV = generateIV()

    # Image path
    imgPath = "C:/Users/shivp/Desktop/CSC321/Asgn-2/resources/cp-logo.bmp"

    # ECB mode
    header, ecb_encrypted = encrypt_bmp(imgPath, "ECB", secret_key, IV)
    save_encrypted_bmp(header, ecb_encrypted, b'', "ECB")

    # CBC mode
    header, cbc_encrypted = encrypt_bmp(imgPath, "CBC", secret_key, IV)
    save_encrypted_bmp(header, b'', cbc_encrypted, "CBC")
