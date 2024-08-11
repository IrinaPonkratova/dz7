'''
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование
должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например
для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
'''

from pathlib import Path
import os


def group_rename(directory:str|Path,final_name:str, count_of_number:int, start_ext:str, final_ext:str, srez:list[int])->None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        # print(f"Ошибка: {directory} не является каталогом.")
        directory.mkdir(parents=True)
    # os.chdir(directory)
    dir_list = sorted(os.listdir(directory))
    print(dir_list)



    start = srez[0]
    fin = srez[1]
    start_num = 0

    for obj in dir_list:
        new_obj = obj.split('.')
        print(new_obj)
        if len(new_obj) == 2 and new_obj[1] == ' '+ start_ext:
            key = new_obj[0]
            if start < 0 or fin > len(key):
                print(f"Ошибка: диапазон {srez} выходит за пределы имени файла '{key}'.")
                continue

            new_name = key[start:fin] +' '+ final_name + str(start_num + 1).zfill(count_of_number) +'.' + final_ext
            # new_name = f'{key[start:fin]}{final_name}{str(start_num + 1).zfill(count_of_number)}.{final_ext}'
            print(new_name)
            # os.rename(f'{key}.{new_obj[1]}',  f'{new_name}.{final_ext}')
            # os.rename(directory / obj, directory/new_name)
            os.rename(os.path.join(directory, obj), os.path.join(directory, new_name))
            start_num += 1

if __name__ == '__main__':
    group_rename('/Users/irina/PycharmProjects/pythonProject1/lesson7/test_dir/spam', 'trash', 2, 'bin', 'txt', [3, 7])

