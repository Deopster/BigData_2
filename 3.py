import numpy, random
print(list(s for i in numpy.random.rand(random.randint(2, 5), random.randint(2, 5)) for s in i))
