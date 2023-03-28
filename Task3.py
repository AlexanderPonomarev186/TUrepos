from PIL import Image
import numpy as np

img = Image.open("2022-12-06.png")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
result_arr = np.zeros((a, a1))  # Пустая матрица размера изображения
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                m1 = arr[n][n1][0]
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = m1 // 100 + n2 // 100 + n3 // 100
                s += M
        s = int(s)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                result_arr[n][n1] = int(
                    s // 50) * 50  # Вместо замены значений в изначальной матрице вставляем значение в заданную в
                # начале пустую
        j = j + 10
    i = i + 10
res = Image.fromarray(result_arr)
res = res.convert('RGB')
res.save('res.png')
