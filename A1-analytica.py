# A1

# Imports ------------------------------------------------------

import aifc
from distutils.log import error
import numpy as np
import math 
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

# Numpy ---------------------------------------------------------

# Iteração - questão 4

# (a)

a = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

a_sum = 0
a_dp1 = 0

for number in a:
    a_sum += number
    #a_sum = number + a_sum

a_avg = a_sum / len(a)

print('a média dos números dessa lista: ', a_avg)

# (b)

for number in a:
    a_dp1 += (number - a_avg)**2 

a_dp2 = math.sqrt((a_dp1) / len(a))

print('o desvio padrão dos números dessa lista: ',a_dp2)

# Funções - Questão 5

# (a)

print(np.sort(a))

# (b)

print(np.shape(a))

# (c)

print(a.mean())

# (d)

print(a.std())
print(a.max())
print(a.min())

# (e)

n = random.randint(11, size=(100))

print(n)

# média
print(n.mean())

# desvio padrao
print(n.std())

# valor máximo
print(n.max())

# valor mínimo
print(n.min())


# Pandas --------------------------------------------

# 1.2.2 Parte Prática 

# Questão 1

dados = pd.read_csv('./Desktop/Analytica/Dataset.csv')
 

# Questão 2

print(dados)

# Questão 3

# (a)

filtro_ano = dados["ano"] == 1991
ano_filtrado = dados[filtro_ano] 

print(ano_filtrado)

# (b)

print(ano_filtrado['expectativa_vida'])

# (c)

print(ano_filtrado['expectativa_vida'].mean())

# Questão 4

# (a)

filtro_idh_maior = ano_filtrado["idhm"] > ano_filtrado['expectativa_vida'].mean()
idh_maior_filtrado = ano_filtrado[filtro_idh_maior]

print(idh_maior_filtrado)

# (b)

print(idh_maior_filtrado["sigla_uf"])

# Questão 5

ano_idhm = ano_filtrado[["ano", "idhm"]]

print(ano_idhm.sort_values(by=['expectativa_vida']))

print(ano_idhm.sort_values(by=['expectativa_vida']).head(5))

# Questão 6

ano_sigla_idhm = ano_filtrado[["ano","sigla_uf", "idhm"]]

idh = ano_filtrado["idhm"] 

idh_min = ano_sigla_idhm[ano_sigla_idhm["idhm"] == idh.min()] 

print(idh_min) 

idh_max = ano_sigla_idhm[ano_sigla_idhm["idhm"] == idh.max()] 

print(idh_max)

idh_idxmin = idh.idxmin() 

print(ano_sigla_idhm.iloc[idh_idxmin])

idh_idxmax = idh.idxmax() 

print(ano_sigla_idhm.iloc[idh_idxmax])

# Matplotlib ------------------------------------------------------------

# Questão 1

estados = (dados.loc[:, 'sigla_uf']).unique()

qnt_pop = ano_filtrado.loc[:, 'populacao_urbana'].values

plt.bar(estados,qnt_pop)
plt.show()

# Questão 2

ano_2000 = dados["ano"] == 2000
ano_2000_filtrado = dados[ano_2000]

ano_2010 = dados["ano"] == 2010
ano_2010_filtrado = dados[ano_2010]

plt.hist(ano_filtrado["idhm"], bins = 10)
plt.show()


plt.hist(ano_2000_filtrado["idhm"], bins = 10)
plt.show()


plt.hist(ano_2010_filtrado["idhm"], bins = 10)
plt.show()

# Questão 3

exp_vida = np.array([dados["expectativa_vida"]])
idh = np.array([dados["idhm"]])

plt.scatter(exp_vida, idh)
plt.show()

"""
De acordo com os pontos observados no Scatter Plot sobre os dados relativos à expectativa de vida e o IDH, podemos ver que o valor dos dois dados vão crescendo mutualmente, ou seja, vão crecendo em conjunto, portanto, existe uma relação direta entre as duas medidas.
"""

# Desafio Final ------------------------------------------------------------------

expec_vida_1991 = ano_filtrado["expectativa_vida"]

expec_vida_2010 = ano_2010_filtrado["expectativa_vida"]

dif_expec_vida = expec_vida_2010.values - expec_vida_1991.values

plt.bar(estados,dif_expec_vida)
plt.show() 

estados_maior_expec = pd.DataFrame({"sigla_uf": estados,"diferenca_expec_vida": dif_expec_vida})

expec_vida_maior10 = estados_maior_expec["diferenca_expec_vida"] >= 10
expec_maior10_filtrado = estados_maior_expec[expec_vida_maior10]

print(expec_maior10_filtrado["sigla_uf"])