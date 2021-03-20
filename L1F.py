from scipy.stats import uniform
from numpy import arange
import matplotlib.pyplot as plt

def number_gen(n):  # Генератор списка чисел
    return uniform.rvs(loc=0, scale=3, size=2 ** n)

def func1(alpha):  # Первая подфункция системы
    return 2 / (alpha + 1)

def func2(alpha):  # Вторая подфункция системы
    return -1 * (2 * alpha - 3)

def func3(alpha):  # Третья подфункция системы
    return 4 * alpha ** 2 - 16 * alpha + 15

if __name__ == "__main__":
    real_integral, emp_integral = [], []
    for power in range(0, 15):  # Перебор степеней 2-ки
        alpha_list = number_gen(power)
        for alpha_ind in range(len(alpha_list)):  # Определение принадлежности каждого числа к одному из отрезков,
            if alpha_list[alpha_ind] < 1:         # и замена элемента на значение функции от него
                alpha_list[alpha_ind] = func1(alpha_list[alpha_ind])
            elif 1 <= alpha_list[alpha_ind] <= 2:
                alpha_list[alpha_ind] = func2(alpha_list[alpha_ind])
            else:
                alpha_list[alpha_ind] = func3(alpha_list[alpha_ind])
        print(alpha_list)
        emp_integral += [(3 / len(alpha_list)) * sum(alpha_list)]  # Интеграл по методу Монте-Карло
        real_integral += [1.71962]
        print(power, "-я степень 2-ки: ", emp_integral[power],
              "\nДлина списка: ", len(alpha_list), sep="")    # Вывод результата
    plt.figure(1)
    plt.plot([i for i in range(15)], emp_integral, label="Метод Монте-Карло")
    plt.plot([i for i in range(15)], real_integral, label="Истинное значение интеграла")
    plt.title("Сравнение истинного и оценочного значения интеграла")
    plt.xlabel("Степень 2-ки")
    plt.ylabel("Значение функции")
    plt.legend()
    plt.grid()
    plt.figure(2)
    plt.plot(arange(0, 1, 0.001), [2 / (x + 1) for x in arange(0, 1, 0.001)])
    plt.plot(arange(1, 2.001, 0.001), [-1 * (2 * x - 3) for x in arange(1, 2.001, 0.001)])
    plt.plot(arange(2.001, 3.001, 0.001), [4 * x ** 2 - 16 * x + 15 for x in arange(2.001, 3.001, 0.001)])
    plt.title("График F_рез")
    plt.grid()
    plt.show()