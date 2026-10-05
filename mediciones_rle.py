import math
import matplotlib.pyplot as plt
from p1 import time_measure, rle_encode_naive, rle_encode_optimized

# 1. Preparación de datos (Pocas rachas vs Muchas rachas)
def prep_muchas_rachas(n):
    # Alterna valores continuamente. Ejemplo: [0, 1, 0, 1, 0, 1...]
    return [i % 2 for i in range(n)]

def prep_pocas_rachas(n):
    # Crea solo dos rachas gigantes. Ejemplo para n=10: [0,0,0,0,0, 1,1,1,1,1]
    mitad = n // 2
    return [0] * mitad + [1] * (n - mitad)

# 2. Tamaños a probar
# Es posible que debas reducir el límite a 5000 si la versión naive tarda demasiado
Nlist = list(range(100, 5000, 500))

# 3. Medición (Evaluando el impacto de crear muchas tuplas)
print("Midiendo naive...")
res_naive = time_measure(rle_encode_naive, prep_muchas_rachas, Nlist, Nrep=50, Nstat=10)

print("Midiendo optimized...")
res_opt = time_measure(rle_encode_optimized, prep_muchas_rachas, Nlist, Nrep=50, Nstat=10)

# 4. Desempaquetar datos
medias_naive = [m for m, v in res_naive]
std_naive = [math.sqrt(v) for m, v in res_naive]

medias_opt = [m for m, v in res_opt]
std_opt = [math.sqrt(v) for m, v in res_opt]

# 5. Dibujar gráfica comparativa
plt.figure(figsize=(10, 6))

# Línea Naive
plt.plot(Nlist, medias_naive, label="Naive (Muchas rachas)", color='#d62728')
plt.fill_between(Nlist, 
                 [max(0, m - s) for m, s in zip(medias_naive, std_naive)], 
                 [m + s for m, s in zip(medias_naive, std_naive)], 
                 color='#d62728', alpha=0.2)

# Línea Optimizada
plt.plot(Nlist, medias_opt, label="Optimized (Muchas rachas)", color='#2ca02c')
plt.fill_between(Nlist, 
                 [max(0, m - s) for m, s in zip(medias_opt, std_opt)], 
                 [m + s for m, s in zip(medias_opt, std_opt)], 
                 color='#2ca02c', alpha=0.2)

plt.xlabel("Tamaño de la lista (n)")
plt.ylabel("Tiempo medio (segundos)")
plt.title("Comparativa de RLE: Naive vs Optimized")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("rle_muchas_rachas.png", dpi=300)
plt.show()