#exercicio 01

import numpy as np

##calcular a distância euclidiana entre as séries
# definição das séries
s1= np.array((168,398,451,337,186,232,262,349,189,204,220,220,207,239,259,258,242,331,251,323,106,1055,170))

s2= np.array((168,400,451,300,186,200,262,349,189,204,220,220,207,239,259,258,242,331,251,180,106,1055,200))

# subtraindo os valores
subtracao = s1 - s2
#print(subtracao)
#Ao quadrado
subtracao_quadrado = subtracao**2
#print(subtracao_quadrado)
#somatorio
somatorio = np.sum(subtracao_quadrado)
print(" A distância Euclidiana entre as séries é:", somatorio)

##calcular a série temporal com os valores médios entre s1 e s2
medias = np.mean([s1,s2], axis=0)
print("Serie temporal referente aos valores médios de s1 e s2 é:", medias)

##calcular a série temporal com os valores máximos de cada instante entre s1 e s2

maximo = np.maximum(s1,s2)

print("Série temporal com valores máx:", maximo)
##calcular a série temporal com os valores mínimos de cada instante entre s1 e s2

minimo = np.minimum(s1,s2)
print("Série temporal com valores min:", minimo)