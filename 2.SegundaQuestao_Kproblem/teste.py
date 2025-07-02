def kClosest(points, K):
    # 1) Ordena a lista de pontos pelo quadrado da distância até a origem
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    
    # 2) Retorna os K primeiros pontos — os mais próximos
    return points[:K]

# Exemplo de uso:
points = [[1,3], [-2,2], [2,-2], [1,1]]
K = 2
print(kClosest(points, K))  # Saída esperada: [[-2,2], [2,-2]]
