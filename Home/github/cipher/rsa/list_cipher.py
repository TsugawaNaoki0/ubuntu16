from cryptography.fernet import Fernet

str1 = ["I am okay", "No thank you !!!", "Hello !!!"]
key = Fernet.generate_key()
token = Fernet(key)


class list_encrypter_class():
    def list_encrypter(self, plainList, token):
        str_list = plainList
        str_list_after = ["" for i in range(len(str_list))]
        for i in range(len(str_list)):
            enctex = token.encrypt(str_list[i].encode())

            str_list_after[i] = enctex

        return str_list_after


class list_decrypter_class():
    def list_decrypter(self, encryptedList, token):
        str_list = encryptedList

        str_list_after = ["" for i in range(len(str_list))]
        for i in range(len(str_list)):

            dectex = token.decrypt(str_list[i])

            str_list_after[i] = dectex

        for k in range(len(str_list_after)):
            str_list_after[k] = str_list_after[k].decode()
        return str_list_after


hello = ["11111", "22222", "33333", "44444", "55555"]
aaa = list_encrypter_class()
bbb = aaa.list_encrypter(hello, token)

ccc = list_decrypter_class()
ddd = ccc.list_decrypter(bbb, token)





from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.txt", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
    [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

# セッションキーをRSA秘密鍵で復号する
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# データをAESセッションキーで復号する
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
