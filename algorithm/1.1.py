import binary_search
import simple_search

list=list(range(1,1000000))
item = 999999
'''
key_1 = binary_search.bina_sc(item, list)
if key_1 != -1:
    print("binary_search: ",key_1)
else:
    print("find nothing")
'''
######################################

key_2 = simple_search.simp_sc(item, list)
if key_2 != -1:
    print("simple_search: ",key_2)
else:
    print("find nothing")
