class Matrix:
    def __init__(self, m, n):
        self.rowCount = m
        self.colCount = n
 
        self.matrix = []
        for i in range(m):
            lis = []
            for j in range(n):
                lis.append(0)
            self.matrix.append(lis)
 
    def set(self, i, j, x):
        self.matrix[i][j] = x
 
    def get(self, i, j):
        return self.matrix[i][j]
 
    def transpose(self):
        trans = Matrix(self.colCount, self.rowCount)
 
        for i in range(self.rowCount):
            for j in range(self.colCount):
                trans.matrix[j][i] = self.matrix[i][j]
 
        return trans
    
    def __add__(self, q):
        if (self.rowCount != q.rowCount) or (self.colCount != q.colCount):
            return None
 
        result = Matrix(self.rowCount, self.colCount)
 
        for i in range(self.rowCount):
            for j in range(self.colCount):
                result.set(i, j, self.matrix[i][j] + q.matrix[i][j])
 
        return result
 
    def __mul__(self, q):
        if self.colCount != q.rowCount:
            return None
 
        result = Matrix(self.rowCount, q.colCount)
 
        for i in range(self.rowCount):
            for j in range(q.colCount):
                total = 0
                for k in range(self.colCount):
                    total += self.matrix[i][k] * q.matrix[k][j]
 
                result.set(i, j, total)
 
        return result
    

 
def read_matrix(m,n):
    mat = Matrix(m,n)
    for i in range(0,m):
        row = input().split()
        for j in range(0,n):
            mat.set(i,j,int(row[j]))
    return mat
 
def print_matrix(mat):
    for i in range(0,mat.rowCount):
        for j in range(0,mat.colCount):
            print(mat.get(i,j),end='')
            if j!=mat.colCount-1:
                print(' ',end='')
        print()
 
mat1 = read_matrix(int(input()), int(input()))
mat2 = read_matrix(int(input()), int(input()))
mat3 = mat1.transpose() * (mat1 + mat2)
print_matrix(mat3)