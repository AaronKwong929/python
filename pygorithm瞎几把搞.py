# https://blog.csdn.net/y472360651/article/details/77881919
# https://pygorithm.readthedocs.io/en/latest/index.html
from pygorithm.sorting import bubble_sort
from pygorithm.sorting import selection_sort
from pygorithm.sorting import heap_sort

list_1 = [1, 43, 58, 12, 5, 79, 2, 90, 72, 85, 45, 23, 50]

sortedList1 = bubble_sort.sort(list_1)  # 冒泡
sortedList1_1 = bubble_sort.improved_sort(list_1)  # 改良冒泡
print(sortedList1)
print(sortedList1_1)
print(bubble_sort.get_code())
print(bubble_sort.time_complexities())
print('\n\n')

sortedList2 = selection_sort.sort(list_1)  #选择排序法
print(sortedList2)
print(selection_sort.get_code())
print(selection_sort.time_complexities())
print('\n\n')

sortedList3 = heap_sort.sort(list_1)  # 堆排序
print(sortedList3)
print(heap_sort.get_code())
print(heap_sort.time_complexities())
print('\n\n')
