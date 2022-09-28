import numpy as np
import matplotlib.pyplot as plt


x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
plt.subplot(2,1,1)
plt.title("Graph of xn")
plt.stem(range(0,6),x)
plt.ylabel('$x(n)$')
plt.grid()

k = 20
y = np.zeros(20)

y = np.loadtxt("./EE3900/Assignment1/Codes/Q3/wa.dat",dtype='double')

print(y)

plt.subplot(2,1,2)
plt.title("Graph of yn")
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()
plt.savefig('../../Figures/Q3/yn.pdf')
# subprocess.run(shlex