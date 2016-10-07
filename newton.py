import math

import numpy

import gauss


def function1(x1, x2):
    # return math.sin(x1 + 1) - x2 - 1
    return math.sin(x1) - x2 - 1.32


def function2(x1, x2):
    # return 2 * x1 + math.cos(x2) - 2
    return math.cos(x2) - x1 + 0.85


def derivative(function, x1, x2, n):
    dx = 1e-9
    if (n == 1):
        return (function(x1 + dx, x2) - function(x1, x2)) / dx

    else:
        return (function(x1, x2 + dx) - function(x1, x2)) / dx


# def derivative1():
#
# def derivative2():
#
# def derivative3():
#
# def derivative4():

def doAlghorithm(n, T, y):
    e = 1e-9
    A = numpy.zeros([2, 3])
    R = numpy.zeros(2)
    i = 0
    b1 = 0
    b2=0

    while 1 == 1:
        i += 1

        A[0][0] = derivative(function1, y[0], y[1], 1)  # расчет матрицы якоби
        A[0][1] = derivative(function1, y[0], y[1], 2)
        A[0][2] = -function1(y[0], y[1])  # находим вектор невязки
        A[1][0] = derivative(function2, y[0], y[1], 1)
        A[1][1] = derivative(function2, y[0], y[1], 2)
        A[1][2] = -function2(y[0], y[1])
        print("Итерация " + str(i))
        print(y)
        R = gauss.gaussFunc(A)  # решаем систему линейных алгебраических уравнений

        y[0] += R[0]
        y[1] += R[1]

        if math.fabs(function1(y[0], y[1])) > math.fabs(function2(y[0], y[1])):
            b1 = math.fabs(function1(y[0], y[1]))
        else:
            b1 = math.fabs(function2(y[0], y[1]))


        b2=math.fabs(R[0])
        print(b2)
        if b2<math.fabs(R[1]):
            b2=math.fabs(R[1])
        # for j in range(len(R)):
        #
        #     if(math.fabs(R[j])>b2):
        #         b2 = math.fabs(R[j])


        print("b1 =" + str(b1) + "    b2 =" + str(b2))
        if (b1 < e or b2 < e):
            break
        print()

    print("ответ:")
    return y
