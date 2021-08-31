class Vector():
    def __init__(self, units, dim):
        self.units = units
        self.dim = dim
    
    def getItems(self):
        return list(self.units)

    def __str__(self):
        string=""
        for u in self.units:
            string += f"{u}\n"
        return string

class Matrix():

    def __init__(self, n, m):

        self.n = n
        self.m = m
        self.struct = []

    def populate(self, list_n):

        temp_vec = Vector(list_n, len(list_n))
        self.struct.append(temp_vec)
        
    def get_vecs(self):
        return self.struct

    def __str__(self):

        string=""
        i = 0
        while i < self.n:
            t_list = []
            for vec in self.struct:
                t_list.append(vec.getItems()[i])
            string+= str(t_list) +"\n"
            i+=1
            
        return string

class Operations():
    def __init__(self):
        pass

    def dot_prod(v1,v2):
        sum = 0
        for n in range(len(v1.getItems())):
            prod = v1.getItems()[n] * v2.getItems()[n]
            sum += prod

        return sum


    def multiply(m1, m2):
        assert type(m1) == type(m2)
        t_units = []
        for m1_vec in m1.get_vecs():
            
            for m2_vec in m2.get_vecs():
                sum = Operations.dot_prod(m1_vec,m2_vec)
                t_units.append(sum)
        res_vec = Vector(t_units, len(t_units))
    
        return res_vec
        

    

m1 = Matrix(3,3)
m1.populate([1,2,3])
m1.populate([2,5,2])
m1.populate([3,7,8])

m2 = Matrix(3,1)
m2.populate([3,4,1])

print(m1, m2)
print(Operations.multiply(m1,m2))

