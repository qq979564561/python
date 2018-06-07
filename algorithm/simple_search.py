def simp_sc(item ,list):
    for number in list:
        if number == item:
            return list.index(number)
    if number == list[-1]:
        return -1
