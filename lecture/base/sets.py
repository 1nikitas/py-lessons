list_ = [10, 20, 30, 40]

list_=set(list_)

list_.add(50)

print(list_)

# [0]<------->add[-1]


# discard - удалить заданный элемент, если он есть в множестве, и ничего не делать, если его нет;
# remove - удалить заданный элемент, если он есть, и породить ошибку KeyError, если нет;
# pop - удалить некоторый элемент из множества и возвратить его как результат.