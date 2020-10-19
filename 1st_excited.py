import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

change = 0.001
N = 1000 # Calculating values for 1000 equidistant points.
Psi = np.zeros(N) # Initialising the wave function with all zeroes.
g2 = 200 # Took an arbitrary value for gamma-square.
v = np.zeros(N)  # Potential array
E = 0.05 # Trial Eigen value (This trial value should be slightly greater than the Eigen value of the previous state for accurate result.)
k2 = g2*(E-v) # Initialising k-square.
l2 = (1.0/(N-1))**2  # Initialising k-square.

def wavefunction(E,k2,N):
    Psi[0] = 0 # Initialising starting two values.
    Psi[1] = 0.008886 # These two values should already be given for the normalised wave function.

    for i in range(2,N): # Applying NUMEROV's Algorithm (As given in pdf).
        Psi[i] = (2*(1-(5.0/12)*l2*k2[i-1])*Psi[i-1]-(1+(1.0/12)*l2*k2[i-2])*Psi[i-2])/(1+(1.0/12)*l2*k2[i])
    return Psi

def Eigen(Ei,change,N): # This function will find the Eigen value which will be very close to the actual Eigen value.
    k2 = g2*(Ei-v)
    wavefunction(Psi,k2,N)
    P1 = Psi[N-1]
    Ei = Ei + change

    while abs(change) > 1e-6: # Setting precision upto 6th decimal place.
        k2=g2*(Ei-v)
        wavefunction(Psi,k2,N)
        P2 = Psi[N-1]
        
        if P1*P2<0: # When sign for P2 changes means the value has crossed x-axis.
            change = -change/2.0

        Ei = Ei + change
        P1 = P2
    return Ei

E = Eigen(E,change,N)
Psi2=Psi**2
I = spi.simps(Psi2,dx=0.001) # Calculating the area of Psi-square using SIMPSON's RULE.

print "The corresponding Eigen value for this state is: "+ str(E)
print "The area under Psi-square is: "+ str(I)

if(I>=0.99 and I<=1.01):
    print "The wavefunction(Psi) is normalised."
else:
    print "The wavefunction(Psi) is not normalised."

plt.xlabel('x') 
plt.ylabel('Psi(x)') 
plt.title('1st excited state , E2 = '+ str(E))

x=[]
for i in range(1,1001):
    x.append(i/1000.0)

plt.plot(x,Psi)
plt.show()