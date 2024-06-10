a =20
#print(a)
#print(type (a))
#print(id(a))
"""b = 20
print(a==b)
print(a is b)"""
"""order = None
print(id(order))
print(order == None)"""



class Car:
    obj = []
    counter = 0
    def __init__(self,model):
         self.model = model
         Car.obj.append(self)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            obj = Car.obj[Car.counter]
            Car.counter += 1
            return obj
        except IndexError:
            Car.counter = 0
            raise StopIteration
Car('mers'),
Car('bmw'),
Car('deawoo')
for car in Car('mers'):
    print(car)          
            
        