def insertion_sort(list_to_sort):
    if len(list_to_sort) > 1:
        for i in range(1, len(list_to_sort)):
            for j in range(i - 1, -1, -1):
                if list_to_sort[i] < list_to_sort[j]:
                    tmp = list_to_sort[i]
                    list_to_sort[i] = list_to_sort[j]
                    list_to_sort[j] = tmp
                    i = j
    return list_to_sort


def selection_sort(list_to_sort):
    if len(list_to_sort) > 1:
        for i in range(0, len(list_to_sort)):
            for j in range(i + 1, len(list_to_sort)):
                if list_to_sort[i] > list_to_sort[j]:
                    tmp = list_to_sort[j]
                    list_to_sort[j] = list_to_sort[i]
                    list_to_sort[i] = tmp
                    j += 1
    return list_to_sort


print(insertion_sort([0, 1, 3, 8, 7, 2, 5, 4, 9, 6]))
print(selection_sort([3, 0, 1, 8, 7, 2, 5, 4, 9, 6]))
