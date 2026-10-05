import random
import math
import matplotlib.pyplot as plt
from p1 import time_measure, has_sum_pair


# 1. Funciones que fabrican los datos de prueba

def prep_sin_pareja(n):
    lst = [random.randint(0, 1000000) for _ in range(n)]
    return (lst, -1)                  # todos positivos: nunca suman -1


def prep_con_pareja(n):
    lst = [random.randint(0, 1000000) for _ in range(n)]
    i, j = random.sample(range(n), 2) # dos posiciones al azar
    lst[i] = -1 - lst[j]              # ahora lst[i] + lst[j] = -1
    return (lst, -1)


# 2. Tamaños que vamos a probar

Nlist = list(range(10, 10001, 500))


# 3. Medir (cada resultado se guarda en su variable)

resultado_con_pareja = time_measure(has_sum_pair, prep_con_pareja, Nlist, Nrep=100, Nstat=20)
resultado_sin_pareja = time_measure(has_sum_pair, prep_sin_pareja, Nlist, Nrep=100, Nstat=20)


# 4. Dibujar la gráfica

medias_con = [m for (m, v) in resultado_con_pareja]
std_con = [math.sqrt(v) for (m, v) in resultado_con_pareja] # Desviación típica

medias_sin = [m for (m, v) in resultado_sin_pareja]
std_sin = [math.sqrt(v) for (m, v) in resultado_sin_pareja] # Desviación típica

plt.plot(Nlist, medias_sin, label="Sin pareja", color='#ff7f0e')
plt.fill_between(Nlist, 
                 [max(0, m - s) for m, s in zip(medias_sin, std_sin)], 
                 [m + s for m, s in zip(medias_sin, std_sin)], 
                 color='#ff7f0e', alpha=0.2)

plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo medio (segundos)")
plt.title("Rendimiento de has_sum_pair")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("has_sum_pair.png", dpi=300)
plt.show()
