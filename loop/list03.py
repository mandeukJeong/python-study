list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_c = [1, 2, 1, 2]
list_c.remove(2)
print(list_c)

list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
print(list_d)

list_e = [52, 273, 103, 32, 275, 1, 7]
list_e.sort()
print(list_e)

list_e.sort(reverse=True)
print(list_e)

list_f = [273, 32, 103, 57, 52]
print(273 in list_f)
