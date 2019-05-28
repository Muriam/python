from dataclasses import dataclass

# считывание матрицы из файла
with open('in.txt') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]

@dataclass
class edgeStruct:
    u: int   			  # нач. вершины
    v: int			    # кон. вершина
    weight: int			# вес ребра

    def __str__(self):
        return f"({self.u}-{self.v}): {self.weight}"

edge = edgeStruct(1, 2, 10) 
print(edge)

edge.weight = 10
print(edge.weight)
