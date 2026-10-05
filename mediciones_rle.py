import math
import matplotlib.pyplot as plt
from p1 import time_measure, rle_encode_naive, rle_encode_optimized

def prep_muchas_rachas(n):
    return [i % 2 for i in range(n)]

def prep_pocas_rachas(n):
    mitad = n // 2
    return [0] * mitad + [1] * (n - mitad)

Nlist = list(range(100, 5001, 500))

# Medimos los cuatro escenarios
print("Midiendo Naive...")
res_naive_muchas = time_measure(rle_encode_naive, prep_muchas_rachas, Nlist, Nrep=20, Nstat=10)
res_naive_pocas = time_measure(rle_encode_naive, prep_pocas_rachas, Nlist, Nrep=20, Nstat=10)

print("Midiendo Optimized...")
res_opt_muchas = time_measure(rle_encode_optimized, prep_muchas_rachas, Nlist, Nrep=20, Nstat=10)
res_opt_pocas = time_measure(rle_encode_optimized, prep_pocas_rachas, Nlist, Nrep=20, Nstat=10)

plt.figure(figsize=(10, 6))

def plot_res(Nlist, res, label, color, linestyle='-'):
    medias = [m for m, v in res]
    stds = [math.sqrt(v) for m, v in res]
    plt.plot(Nlist, medias, label=label, color=color, linestyle=linestyle, linewidth=2)
    plt.fill_between(Nlist, [max(0, m-s) for m,s in zip(medias, stds)], [m+s for m,s in zip(medias, stds)], color=color, alpha=0.1)

# Dibujamos las 4 curvas
plot_res(Nlist, res_naive_muchas, "Naive (Muchas rachas)", "#d62728")      
plot_res(Nlist, res_opt_muchas, "Optimized (Muchas rachas)", "#2ca02c")    
plot_res(Nlist, res_naive_pocas, "Naive (Pocas rachas)", "#ff7f0e", '--')  
plot_res(Nlist, res_opt_pocas, "Optimized (Pocas rachas)", "#1f77b4", '--')

plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo medio (segundos)")
plt.title("Comparativa completa de RLE")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("rle_completo.png", dpi=300)
plt.show()