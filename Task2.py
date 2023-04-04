import matplotlib.pyplot as plt
import numpy as np
import random
from timer import Timer


def bubble_sort(start_nums):
    nums = start_nums
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


def selection_sort(start_nums):
    nums = start_nums
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

def partition(start_nums, low, high):
    nums = start_nums
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(start_nums):
    nums = start_nums
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

timer = Timer()
def randommass(number_of_nums:int):
    return [random.randint(1,1000) for i in range(number_of_nums)]
test_numbers = [10,20, 30, 100,  1000, 10000, 20000]
timer_1 = []
timer_2 = []
timer_3 = []
for num in test_numbers:
    timer.start()
    bubble_sort(randommass(num))
    timer_1.append(timer.stop())
for num in test_numbers:
    timer.start()
    selection_sort(randommass(num))
    timer_2.append(timer.stop())
for num in test_numbers:
    timer.start()
    quick_sort(randommass(num))
    timer_3.append(timer.stop())
plt.plot(test_numbers, timer_1)
plt.plot(test_numbers,timer_2)
plt.plot(test_numbers,timer_3)
plt.show()
