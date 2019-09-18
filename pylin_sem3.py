#Написать рекурсивную функцию, которая разворачивает последоательность вложенных списков в один с сохранением последовательности элементов
def rec(x):
    new_list = []
    for i in x:
        if type(i) is list:
            #rec(i)
            new_list.extend(rec(i))
        else:
            new_list.append(i)
    return new_list
