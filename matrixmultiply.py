class Vector():

    def __init__(self, R, nums):
        self.R = R
        self.k = nums

    def getItems(self):
        return self.k

    def dotProd(self, vec):
        print(type(vec))
        assert len(self) == len(vec)
        i = 0
        sum = 0
        while i < len(vec):
            sum += (self.k[i]*vec.k[i])
            i += 1
        return sum

    def __len__(self):
        return len(self.k)
    def __str__(self):
        return str(self.k)

class Matrix():

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.R = None
        self.struct = []   
        """
        self.identity = bool
        self.invertible = bool
        self.diagonalizable = bool
        self.determinant = int
        self.basis = Vector
        """
          
    def populate(self, colVec):

        self.R = len(colVec)
        for i in range(self.R):
            if len(self.struct) != self.R:
                self.struct.append([])
            
            self.struct[i].append(colVec.getItems()[i])    

        for list_vec in self.struct:
            list_vec = Vector(self.R, list_vec)


    def get_col_vecs(self):
        assert self.n >= 1
        col_vecs = []
        for i in range(self.R):
            vec = []
            for k in range(self.R):
                vec.append(self.struct[k][i])
            col_vecs.append(Vector(self.R, vec))
        return col_vecs

    def get_row_vecs(self):
        assert self.m >= 1
        row_vecs = []
        for vec in self.struct:
            row_vecs.append(Vector(self.R, vec))

        return row_vecs
    
    def multiply(self, Matrix):
        assert self.m == Matrix.n    


    def transpose(self):
        pass

    def __len__(self):
        return len(self.struct)
        
    def __str__(self):
        string = ""
        
        for v in self.struct:
            string += str(v)
            string += "\n"
        return string
    

if __name__ == "__main__":
    v1 = Vector(3,[1,1,1])    
    v2 = Vector(3,[2,2,2])
    v3 = Vector(3,[3,3,3])

    vecs = [v1,v2,v3]

    matrix = Matrix(3,3)
    for vec in vecs:
     
        matrix.populate(vec)
    
    # print(matrix)

    # cols = matrix.get_col_vecs()
  
    # for col in cols:
    #     print(col, type(col))

    # print('-------')
    # rows = matrix.get_row_vecs()
    # for row in rows:
    #     print(row, type(row))
    # print(rows)

  

