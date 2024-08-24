# def test_func(*params):
#     print("Тип:", type(params))
#     print("Аргумент:", params)
#
# #
# # test_func(1, 2, 3, 4)
#
# def summator(txt, *values, type="sum"):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
#
#
# print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))


# def info(value, *types, names_author="Den", **values):
#     print("Тип:", type(values))
#     print("Аргумент:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
# info("Пример использования параметров всех типов", 2, 3, 4, names_author="Denis", name="Den", course="Python")


# def my_sum(n, *args, txt="Сумма чисел"):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n
#     print(txt + ":", s)
#
#
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")

def single_root_words(root_words, *other_words):
    same_words = []
    other_words2 = list(other_words)

    for i in range(len(other_words2)):
        if root_words.lower() in other_words2[i].lower() or other_words2[i].lower() in root_words.lower():
            same_words.append(other_words2[i])
    return (same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
