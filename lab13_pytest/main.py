from typing import List, Tuple

def bubblesort(lst: List) -> Tuple:
    sorted_lst = list.copy(lst)
    list_len = len(lst)
    num_of_comparisons = 0
    while list_len > 1:
        swapped = False
        for i in range(1, list_len):
            num_of_comparisons += 1
            if sorted_lst[i-1] > sorted_lst[i]:
                sorted_lst[i-1], sorted_lst[i] = sorted_lst[i], sorted_lst[i-1]
                swapped = True

        if not swapped:
            break
        list_len -= 1

    return sorted_lst
