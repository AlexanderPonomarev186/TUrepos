import numpy as np


def permutations(nums: list | tuple | range) -> list:
    nums = list(nums)

    # Функция для генерации перестановок
    def __backtrack(start):
        # Если достигнут конец массива, добавляем текущую перестановку в результат
        if start == len(nums) - 1:
            result.append(nums[:])
        else:
            for i in range(start, len(nums)):
                # Обменяем текущий элемент с каждым из последующих элементов
                nums[start], nums[i] = nums[i], nums[start]
                # Генерируем перестановки для подмассива, начинающегося со следующего элемента
                __backtrack(start + 1)
                # Восстанавливаем исходный порядок элементов
                nums[start], nums[i] = nums[i], nums[start]

    result = []
    __backtrack(0)  # Начинаем с первого элемента массива
    return result


# Вычисление расстояние между элементами в перестановке
def compute_permutation_distance(distance_matrix: np.array, permutation: list) -> float:
    ind1 = permutation  # Путь в прямом направлении
    ind2 = permutation[1:] + permutation[:1]  # Путь в обратном направлении
    return distance_matrix[ind1, ind2].sum()  # Расстояние в двух направлениях


# Решение задачи коммивояжера
def solve_tsp(distance_matrix: np.array) -> tuple[list, int]:
    points = range(1, distance_matrix.shape[0])  # Точки пунктов назначений (кроме нулевой)
    best_distance = np.inf
    best_permutation = None
    for partial_permutation in permutations(points):  # Перебор всех перестановок
        permutation = [0] + list(partial_permutation)  # Точки пунктов назначений с нулевой точкой
        distance = compute_permutation_distance(distance_matrix, permutation)  # Вычисление дистанции в перестановке
        if distance < best_distance:  # Поиск наилучшей
            best_distance = distance
            best_permutation = permutation

    # Возвращаем лучшую найденную перестановку и дистанцию маршрута
    return best_permutation, best_distance


# Матрица узлов маршрутов с дистанциями между точками
path_matrix = np.array([[0, 8, 4, 10],
                        [8, 0, 7, 5],
                        [4, 7, 0, 3],
                        [10, 5, 3, 0]])

path, dist = solve_tsp(path_matrix)
print(path, dist)
