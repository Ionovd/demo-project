# Упорядоченный массив целых чисел arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return print("Element found")
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return print("Element not found")


binary_search(arr, 11)

# дана бинарная строка длины N, состоящая только из нулей и единиц. Гарантируется, что самый левый её элемент 0, а самый правый — 1. Найдите любое вхождение подстроки “01”

N = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]

N_0 =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

def find_01(N):
    left, right = 0 , len(N)
    while left < right:
        mid = (left + right) // 2
        if N[mid] == 0 and N[mid + 1] == 1:
            return print("Element found")
        elif N[mid] == 0:
            left = mid + 1
        else: 
            right = mid
    return print("Element not found")

find_01(N_0)