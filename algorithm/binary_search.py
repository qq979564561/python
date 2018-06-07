def bina_sc(item, list):
    """二分查找 """
    high = len(list)-1
    low = 0
    while high >= low:
        mid = (high + low)
        guess = list[mid]
        if item == guess:
            return mid
        if item > guess:
            low = mid + 1
        if item < guess:
            high = mid - 1
    if low > high:
        return -1
