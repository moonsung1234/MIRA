
import numpy as np
from PIL import Image
from random import *

class Crypto :
    def __init__(self, table_range=1000) :
        self.table_range = table_range

    def __create_table(self, data) :
        return [randrange(1, self.table_range) for _ in range(len(data))]

    def __create_image_table(self, data) :
        length = data.shape[0] * data.shape[1]

        return [
            [
                randrange(int(self.table_range / 10), self.table_range),
                randrange(1, int(self.table_range / 10)),
                randrange(1, int(self.table_range / 100)),
                randrange(1, int(self.table_range / 100))
            ] for _ in range(length)
        ]

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

    def __encrypt_image(self, data) :
        table = np.array(self.__create_image_table(data))
        float_data = data.reshape((data.shape[0] * data.shape[1], data.shape[2]))
        encrypted_data = float_data + table[:, 0].reshape(-1, 1)
        encrypted_data = float_data - table[:, 1].reshape(-1, 1)
        encrypted_data = float_data * table[:, 2].reshape(-1, 1)
        encrypted_data = float_data / table[:, 3].reshape(-1, 1)

        return encrypted_data.reshape((data.shape[0], data.shape[1], data.shape[2])).astype(np.uint8), table.tolist()

    def encrypt(self, data) :
        return self.__encrypt(data)

    def encrypt_file(self, file_name) :
        file1 = open(file_name, "r", encoding="utf-8")
        data = ""

        while True :
            line = file1.readline()

            if not line :
                break

            data += line

        result, table = self.__encrypt(data)

        file2 = open(file_name, "w", encoding="utf-8")
        file2.write(result)

        return result, table

    def encrypt_image(self, data) :
        return self.__encrypt_image(data)

    def encrypt_image_file(self, file_name) :
        img = Image.open(file_name)
        img_arr = np.array(img)

        result, table = self.__encrypt_image(img_arr)

        result_img = Image.fromarray(result)
        result_img.save(file_name)

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
        file1 = open(file_name, "r", encoding="utf-8")
        data = ""

        while True :
            line = file1.readline()

            if not line :
                break

            data += line

        result = self.__decrypt(data, table)

        file2 = open(file_name, "w", encoding="utf-8")
        file2.write(result)

        return result