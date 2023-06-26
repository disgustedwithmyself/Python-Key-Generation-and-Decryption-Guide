from cryptography.fernet import Fernet

Чтение ключа из файла
with open('mykey.key', 'rb') as file:
key = file.read()

Создание объекта Fernet с помощью ключа
fernet = Fernet(key)

Зашифрование данных
data = b'My secret message'
encrypted_data = fernet.encrypt(data)

Расшифровка данных
decrypted_data = fernet.decrypt(encrypted_data)
print(decrypted_data)
