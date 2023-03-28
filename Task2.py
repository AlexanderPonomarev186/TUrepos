import matplotlib.pyplot as plt
import numpy as np
import random
from timer import Timer


def bubble_sort(start_nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    nums = start_nums
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return nums


def selection_sort(start_nums):
    # Значение i соответствует кол-ву отсортированных значений
    nums = start_nums
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

def partition(start_nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
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

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]
    return nums

def quick_sort(start_nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    nums = start_nums
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

timer = Timer()
mass_1 = [random.randint(1,1000) for i in range(10)]
mass_2 = [random.randint(1,1000) for g in range(1000)]
mass_3 = [random.randint(1,1000) for k in range(10000)]
mass_of_mass = [mass_1, mass_2, mass_3]
timer_1 = []
timer_2 = []
timer_3 = []
for mass in mass_of_mass:
    timer.start()
    bubble_sort(mass)
    timer_1.append(timer.stop())
for mass in mass_of_mass:
    timer.start()
    selection_sort(mass)
    timer_2.append(timer.stop())
for mass in mass_of_mass:
    timer.start()
    quick_sort(mass)
    timer_3.append(timer.stop())
plt.plot(timer_1, [10, 1000, 10000])
plt.plot(timer_2, [10, 1000, 10000])
plt.plot(timer_3, [10, 1000, 10000])
plt.show()
