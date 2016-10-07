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



def doAlghorithm(approach):
    e = 1e-9
    jacobi = numpy.zeros([2, 3])
    vectorOfx = numpy.zeros(2)
    i = 0
    b1 = 0
    b2=0

    while 1 == 1:
        i += 1

        jacobi[0][0] = derivative(function1, approach[0], approach[1], 1)  # расчет матрицы якоби
        jacobi[0][1] = derivative(function1, approach[0], approach[1], 2)
        jacobi[0][2] = -function1(approach[0], approach[1])  # находим вектор невязки
        jacobi[1][0] = derivative(function2, approach[0], approach[1], 1)
        jacobi[1][1] = derivative(function2, approach[0], approach[1], 2)
        jacobi[1][2] = -function2(approach[0], approach[1])
        print("Итерация " + str(i))
        print(approach)
        vectorOfx = gauss.gaussFunc(jacobi)  # решаем систему линейных алгебраических уравнений

        approach[0] += vectorOfx[0]
        approach[1] += vectorOfx[1]

        if math.fabs(function1(approach[0], approach[1])) > math.fabs(function2(approach[0], approach[1])):
            b1 = math.fabs(function1(approach[0], approach[1]))
        else:
            b1 = math.fabs(function2(approach[0], approach[1]))


        b2=math.fabs(vectorOfx[0])
        print(b2)
        if b2<math.fabs(vectorOfx[1]):
            b2=math.fabs(vectorOfx[1])
        # for j in range(len(R)):
        #
        #     if(math.fabs(R[j])>b2):
        #         b2 = math.fabs(R[j])


        print("b1 =" + str(b1) + "    b2 =" + str(b2))
        if (b1 < e or b2 < e):
            break
        print()

    print("ответ:")
    return approach
