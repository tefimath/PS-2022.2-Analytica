# A1

# Numpy ----------------------

import numpy as np
import math 
from numpy import random
import pandas as pd


# # Iteração - questão 4

# #(a)

# a = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

# a_sum = 0
# a_dp1 = 0

# for number in a:
#     a_sum += number
#     #a_sum = number + a_sum

# a_avg = a_sum / len(a)

# print('a média dos números dessa lista: ', a_avg)

# #(b)

# for number in a:
#     a_dp1 += (number - a_avg)**2 

# a_dp2 = math.sqrt((a_dp1) / len(a))
# #a_avg = a_sum / len(a)

# print('o desvio padrão dos números dessa lista: ',a_dp2)

# # Funções - questão 5

# #(a)

# print(np.sort(a))

# #(b)

# print(np.shape(a))

# #(c)

# print(a.mean())

# #(d)

# print(a.std())
# print(a.max())
# print(a.min())

# #(e)


# n = random.randint(11, size=(100))

# print(n)

# # média
# print(n.mean())

# # desvio padrao
# print(n.std())

# # valor máximo
# print(n.max())

# # valor mínimo
# print(n.min())


# Pandas ----------------------

dados = pd.read_csv('./')
