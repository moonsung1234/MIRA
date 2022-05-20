
from random import *

class Crypto :
    def __init__(self, table_range=1000) :
        self.table_range = table_range

    def __create_table(self, data) :
        return [randrange(1, self.table_range) for _ in range(len(data))]

    def __encrypt(self, data) :
        table = self.__create_table(data)
        encrypted_data_list = [str(ord(data[i]) * table[i])  for i in range(len(data))]
        result = ""

        for i in range(len(encrypted_data_list)) :
            if i == len(encrypted_data_list) - 1 :
                result += encrypted_data_list[i]

            else :
                result += encrypted_data_list[i] + " "

        return result, table

    def encrypt(self, data) :
        return self.__encrypt(data)

    def encrypt_file(self, file_name) :
        file = open(file_name, "r", encoding="utf-8")
        data = ""

        while True :
            line = file.readline()

            if not line :
                break

            data += line

        result, table = self.__encrypt(data)

        file = open(file_name, "w", encoding="utf-8")
        file.write(result)

        return result, table

    def __decrypt(self, encrypted_data, table) :
        encrypted_data_list = encrypted_data.split(" ")
        decrypted_data_list = [chr(int(int(encrypted_data_list[i]) / table[i])) for i in range(len(encrypted_data_list))]

        result = ""

        for c in decrypted_data_list :
            result += c

        return result

    def decrypt(self, encrypted_data, table) :
        return self.__decrypt(encrypted_data, table)

    def decrypt_file(self, file_name, table) :
        file = open(file_name, "r", encoding="utf-8")
        data = ""

        while True :
            line = file.readline()

            if not line :
                break

            data += line

        result = self.__decrypt(data, table)

        file = open(file_name, "w", encoding="utf-8")
        file.write(result)

        return result