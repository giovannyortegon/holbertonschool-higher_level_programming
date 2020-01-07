#!/usr/bin/python3
"""  """
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    else:
        r_arr = len(list_of_integers)
        arr = list_of_integers
        piv = 0
        for idx in range(r_arr):
            if idx == 0 and arr[idx] > idx + 1:
                piv = arr[idx]
            elif arr[idx - 1] < arr[idx] and arr[idx] > arr[idx + 1]:
                piv = arr[idx]
            elif idx == r_arr and arr[idx] > piv and arr[idx] > arr[idx - 1]:
                piv = arr[idx]
            else:
                pass
        return piv
