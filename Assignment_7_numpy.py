#1
import numpy as np
print(np.__version__)

#2
import numpy as np
x = np.arange(10)
print("> array(", x, ")")

#3
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

#4
np.argwhere(iris[:, 3].astype(float) > 1.0)[0]

#5
np.random.seed(100)
a = np.random.uniform(1,50, 20)

print(np.where(a < 10, 10, np.where(a > 30, 30, a)))