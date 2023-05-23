import numpy as np
from pylab import *
from scipy.special.orthogonal import p_roots


def monte_carlo_method(func, a=0,b=1, n=1000):
    subsets = np.arange(0, n+1, n/10)
    u = np.zeros(n)
    for i in range(10): # выборка случайной величины u
        start = int(subsets[i])
        end = int(subsets[i+1])
        u[start:end] = np.random.uniform(low=i/10, high=(i+1)/10, size=end-start)
    np.random.shuffle(u)
    # В методе Монте-Карло искомую функцию f(x) выражают, как (b-a)*M(u), где M(u)-математичекое ожидание
    # случайной величины u
    # Формула вычисления интеграла будет (b-a)*M(u) = ((b-a)/n)*sum(u)
    # Момент - из-за случайной величины в формуле, может выдавать не точный результат

    u_func = func(a+(b-a)*u)

    s = ((b-a)/n)*u_func.sum()

    return s

# def gauss_chebyshev(f, a, b, n):
#     """Вычисляет определенный интеграл функции f на интервале [a, b]
#        с помощью формулы Гаусса-Чебышева порядка n.
#     """
#     x = np.cos(np.pi * (np.arange(1, n+1) - 0.5) / n) # вычисляем узлы Чебышева
#     t = 0.5 * (b - a) * x + 0.5 * (b + a)              # переводим узлы на интервал [a, b]
#     w = np.pi / n                                     # вычисляем веса
#     integral = np.sum(w * f(t))                       # вычисляем сумму взвешенных значений функции
#     return 0.5 * (b - a) * integral                    # умножаем на половину длины интервала

def trapezoidal_rule(f, a, b, n):
    # метод трапеций
    h = (b - a) / n # Делим отрезок [a,b] на равные n отрезков h по (b-a)/n
    sum = h * ((f(a)/2) + (f(b)/2))
    for i in range(1, n):
        x = a + i * h
        sum += f(x)*h #Применяем функцию для каждого отрезка отдельно, умножаем на длину и складываем
    return sum


def rectangle_rule(f, a, b, n):
    # метод прямоугольников
    h = (b - a) / n # Делим отрезок [a,b] на равные n отрезков h по (b-a)/n
    sum = 0
    for i in range(0, n):
        x = a + h/2 +i * h
        sum += f(x)*h #Применяем функцию для каждого отрезка отдельно, умножаем на длину и складываем
    return sum

def rectangle_right_rule(f, a, b, n):
    # метод прямоугольников
    h = (b - a) / n # Делим отрезок [a,b] на равные n отрезков h по (b-a)/n
    sum = 0
    for i in range(0, n):
        x = a +i * h
        sum += f(x)*h #Применяем функцию для каждого отрезка отдельно, умножаем на длину и складываем
    return sum

def simpson_rule(f, a, b, n):
    # Метод Симпсона(метод трапеций) Это тож по формуле
    h = (b-a)/6
    sum = f(a+(((b-a)*(2*n))/(2*n))) + f(a+((b-a)/(2*n)))
    for i in range(1, 2*n -1, 2):
        sum+=4*f(a+(((b-a)*i)/(2*n))) # Разбиваем отрезок на 2n равных частей, нечетные отрезки умножем на 4, четные - на 2, и складываем
    for i in range(2, 2*n - 2, 2):
        sum+=2*f(a+(((b-a)*i)/(2*n)))
    return sum*h/n # Сумму умножаем на h и делим на n

def gauss(f,n,a,b):
    [x,w] = p_roots(n+1) # Метод Гаусса. Я хз, как объяснить, но работает
    G=0.5*(b-a)*sum(w*f(0.5*(b-a)*x+0.5*(b+a)))
    return G
def f(x):
    return x**2  # Функция, которую мы будем интегрировать

print(trapezoidal_rule(f, 0,1,1000))
print(rectangle_rule(f, 0,1,1000))
print(simpson_rule(f,0,1,1000))
print(monte_carlo_method(f, 0, 1, 1000))
print(gauss(f, 5, 0, 1))
# print(gauss_chebyshev(f, 0, 1, 5))
