from . matrixmultiply import Matrix, Vector

class Identity(Matrix):
    
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.m = n
        self.self_pop()

    def self_pop(self):
        
        for i in range(n):
            vec = []
            for k in range(n):

                if i == k:
                    vec.append(1)
                else:
                    vec.append(0)
            self.struct.append(vec)
