# Сортировка выбором
from typing import List


def findSmallest(arr:List[int], flag:str) -> int:
    smallest = arr[0]  # для хранения значения
    smallest_index = 0  # для хранения индекса значения

    for i in range(1, len(arr)):
        if flag == '<':
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        else:
            if arr[i] > smallest:
                smallest = arr[i]
                smallest_index = i

    return smallest_index


def selectionSort(arr:List[int], flag:str) -> List[int]:  # сортирует массив
    '''flag указывает в какую сторону сортировать массив'''
    newArr = []

    for i in range(len(arr)):  # Находит наименьший элемент в массиве
        smallest = findSmallest(arr, flag)  # и добавляет его в новый массив
        newArr.append(arr.pop(smallest))

    return newArr


print(selectionSort([5, 3, 6, 2, 10], '<'))  # выведет отсортированный массив в порядке
# возрастания in
print(selectionSort([5, 3, 6, 2, 10], '>'))  # выведет отсортированный массив в порядке
# убывания

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         def findSmallest(nums: List[int]) -> int:
#             smallest = nums[0]
#             smallest_index = 0
#
#             for i in range(1, len(nums)):
#                 if nums[i] < smallest:
#                     smallest = nums[i]
#                     smallest_index = i
#
#             return smallest_index
#
#         def selectionSort(nums: List[int]) -> List[int]:
#             newArr = []
#
#             for i in range(len(nums)):
#                 smallest = findSmallest(nums)
#                 newArr.append(nums.pop(smallest))
#
#             return newArr
#
#         return selectionSort(nums)

# print(selectionSort(nums))


# if __name__ == '__main__':
#     c = Solution()
#     nums = [2, 0, 2, 1, 1, 0]
#     print(c.sortColors(nums))
    # print(Solution.sortColors(0,nums))