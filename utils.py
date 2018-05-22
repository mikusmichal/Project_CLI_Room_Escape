import os


def clear_screen():
    os.system('cls')


def in_both_arrays(array_1, array_2):
    result_array = []
    for item in array_1:
        if item in array_2:
            result_array.append(item)
    return result_array
