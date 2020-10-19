E1 = 0.0493486328125
E2 = 0.197391601563
E3 = 0.444131835938
E4 = 0.789567382813
E5 = 1.23370019531

import numpy as np
import matplotlib.pyplot as plt

E_1=[]
E_2=[]
E_3=[]
E_4=[]
E_5=[]

for i in range(1000):
    E_1.append(E1)
    E_2.append(E2)
    E_3.append(E3)
    E_4.append(E4)
    E_5.append(E5)

plt.ylabel('E_n') 
plt.title('Comparison graph for Eigen values.')

plt.plot(range(1000),E_1)
plt.plot(range(1000),E_2)
plt.plot(range(1000),E_3)
plt.plot(range(1000),E_4)
plt.plot(range(1000),E_5)

plt.show()
