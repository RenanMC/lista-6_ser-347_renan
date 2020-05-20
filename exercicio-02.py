#Exercicio 02

import matplotlib as mpl

import matplotlib.pyplot as plt

# Grupos de Idade
ano = ["0-4", "5-9", "10-14","15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89","90-94","95-99","100"]
num_pop = [6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

x_pos = [ x for x in range( len(ano) ) ]

plt.figure( figsize=(10, 8) )

plt.bar(x_pos, num_pop, align='center',
        color='Crimson', linewidth=2, edgecolor='black')

plt.yticks([ 0, 500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000, 5500000, 6000000, 6500000, 7000000, 7500000,8000000, 8500000, 9000000, 9500000],
            )

plt.xticks(x_pos, ano, rotation=45)

plt.title("Distribuição da População Feminina")

plt.xlabel("Grupos de Idade")
plt.ylabel("População Feminina")

plt.grid(b=True, color='gray', linestyle='--', linewidth=0.5);