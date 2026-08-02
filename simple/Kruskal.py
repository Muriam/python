# считывание матрицы из файла
with open('input.txt') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]

# алгоритм Краскала
def kruskal():
    N = len(matrix)                      # N - кол-во вершин, берется из матрицы
    Edges = []                           # объявление списка ребер Edges    
    for i in range(1, N):                # перебираю вершины, в диапазоне от 1 до N по строкам
        for j in range(i, N):            # и по столбцам
            weight = matrix[i][j]        # присваиваю весу значение из матрицы
            if i != j and weight == 0:   # нулевой вес для отличных друг от друга не смежных вершин обозначается нулевым весом
                continue                 # пропустить итерацию если (у элемента матрицы не одинаковый индекс по столбцу и строке) И (вес = 0)
            Edges.append([weight, i, j]) # иначе добавить ребро в список ребер         
    M = len(Edges)                       # М - кол-во ребер, присваиваю из списка ребер 
    Edges.sort()		         		 # СОРТРИРОВКА РЁБЕР  
    Comp = list(range(N))	             # Comp - это компонента связности
    Ostov = []                          # список ребер, составляющих остов
    Ans = 0                             # Ans - хранит общее кол-во весов
    for weight, start, end in Edges:      # для каждого ребра в списке ребер Edges
        Ostov.append([weight, i, j])    # добавление ребра с список 
        if Comp[start] != Comp[end]:	 # если ребро соединяет две разные компоненты связности...  
            Ans += weight	             # 		 
            a = Comp[start]		         #			
            b = Comp[end]		         #			
            for i in range(N): 		      # перебираю вершины, в диапозоне от 1 до N
                if Comp[i] == b:	     # ...всем вершинам, которые раньше находились в компоненте b		
                    Comp[i] = a          # ...изменить номер компоненты на a
    return Ans, Ostov


Ans, Ostov = kruskal()

print('Вес: ', Ans) 
print('Остов ', *Ostov) 
