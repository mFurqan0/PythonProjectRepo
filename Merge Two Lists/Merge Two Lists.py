import heapq

list1 = [1,2,3,4,56,8]
list1.sort()
list2 = [321,354,68,73,]
list2.sort()
merge_list = list(heapq.merge(list1,list2))

print(merge_list)
