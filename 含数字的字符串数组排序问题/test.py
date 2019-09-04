import re

re_digits = re.compile(r'(\d+)')


def emb_numbers(s):
    pieces = re_digits.split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces


def sort_strings_with_emb_numbers(alist):
    aux = [(emb_numbers(s), s) for s in alist]
    aux.sort()
    return [s for __, s in aux]


#内置方式调用排序
def sort_strings_with_emb_numbers2(alist):
    return sorted(alist, key=emb_numbers)


list1 = ['f10', 'f2', 'f1']
print('初始列表：')
print(list1)
print('普通排序结果：')
print(sorted(list1))
print('排序之后结果：')
print(sort_strings_with_emb_numbers(list1))
