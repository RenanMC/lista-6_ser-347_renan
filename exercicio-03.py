#Exercicio 02

import matplotlib as mpl

import matplotlib.pyplot as plt

# Grupos de Idade
ano = ["0-4", "5-9", "10-14","15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-94","95-99","100"]
num_pop = [7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

plt.figure( figsize=(10, 8) )

plt.barh(ano, num_pop, color= 'blue')

plt.title("Distribuição da População Masculina")
plt.xlabel("População Masculina")
plt.ylabel("Grupos de Idade")

