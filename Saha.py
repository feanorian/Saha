"""
Craig Brooks
Stellar Structures
Code for Saha Equation Calculations Beta
"""


import scipy.constants as sp
import numpy as np
import matplotlib.pyplot as plt
import sys

#array storing the temperature range
T = np.arange(1, 100000, 1000)
#stores N2/N1 values over entire temperature range
n_Array1 = []
#stores N3/N2 values over entire temperature range
n_Array2 = []
#stores Ni/N_Total values over enture temperature range

N_T1 = []
N_T2 = []
N_T3 = []

#This function calculates both the fractions of ionized Helium in Problem 8.10
def Saha():
#Calculates N2/N1 from 1 to 60000 degrees
	for x in T:
		N1 = ((4 * sp.Boltzmann * x)/20) * np.power((2 * sp.pi * sp.m_e * sp.Boltzmann * x)/(np.power(sp.Planck,2)),1.5) * np.exp(-3.941354e-18/(1.38e-23 * x))
		n_Array1.append(N1)

 #Calculates N3/N2 from 1 to 60000 degrees
	for y in T:
		N2 = ((sp.Boltzmann * y)/20) * np.power((2 * sp.pi * sp.m_e * sp.Boltzmann * y)/(np.power(sp.Planck,2)),1.5) * np.exp(-8.715841e-18/(1.38e-23 * y))
		n_Array2.append(N2)

	
#Prints value for N1 and N2 for 5000, 15000, and 25000 Kelvin
	print 'NII/NI at 5000 Kelvin %s' % str(n_Array1[5])
	print 'NII/NI at 15000 Kelvin %s' % str(n_Array1[15])
	print 'NII/NI at 25000 Kelvin %s' % str(n_Array1[25])

	print 'NIII/NII at 5000 Kelvin %s' % str(n_Array2[5])
	print 'NIII/NII at 15000 Kelvin %s' % str(n_Array2[15])
	print 'NIII/NII at 25000 Kelvin %s' % str(n_Array2[25])

#function to plot the relative density for N1/Nt, N2/Nt, or N3/Nt
def pdense():
	plot_density = raw_input('Please enter relative density you wish to calculate: NI/NT, NII/NT, NIII/NT:   ')
	if plot_density == 'N1':
		for i in range(len(T)):
			C = 1/(1 + n_Array1[i] + n_Array1[i] * n_Array2[i])
			N_T1.append(C)

		plt.plot(T,N_T1)
		plt.title('N1/N_Total vs Temperature')
		plt.xlabel('Temperature (K)')
		plt.ylabel('N1/N_Total')
		plt.show()
		plt.close()
	if plot_density == 'N2':
		for j in range(len(T)):
			D = n_Array1[j]/(1 + n_Array1[j] + n_Array1[j] * n_Array2[j])
   			N_T2.append(D)
		plt.plot(T,N_T2)
		plt.title('N2/N_Total vs Temperature')
		plt.xlabel('Temperature (K)')
		plt.ylabel('N2/N_Total')
		plt.show()
		plt.close()
	if plot_density == 'N3':
		for k in range(len(T)):
			E = n_Array1[k] * n_Array2[k]/(1 + n_Array1[k] + n_Array1[k] * n_Array2[k])
			N_T3.append(E)
		plt.title('N3/N_Total vs Temperature')
		plt.xlabel('Temperature (K)')
		plt.ylabel('N3/N_Total')
		plt.plot(T,N_T3)
		plt.show()
		plt.close()
	elif plot_density == -1 :
		sys.exit()
#This Function calculates fraction of ionized hydrogen N2/NT in Problem 8.12
def Saha2():
	T = raw_input('Enter temperature:   ')
	Z1 = raw_input('Enter Z1:   ')
	Z2 = raw_input('Enter Z2:   ')
	E_1 = raw_input('Enter Energy (in eV):   ')
	E = float(E_1) * 1.6e-19


	N2 = (2/6.1e31) * float(Z2)/float(Z1) * np.power((2 * sp.pi * sp.m_e * sp.Boltzmann * float(T))/(np.power(sp.Planck,2)),1.5) * np.exp(-E/(1.38e-23 * float(T)))
	N_T = N2/(1 + N2)
	print 'The fraction of ionized H is %s ' % str(N_T)

"""
Problem 8.10a code results from Saha()
	NII/NI at 5000 Kelvin 1.85869910686e-18
	NII/NI at 15000 Kelvin 0.990153710555
	NII/NI at 25000 Kelvin 7204.29737438
	NIII/NII at 5000 Kelvin 4.18745402163e-49
	NIII/NII at 15000 Kelvin 2.38364198105e-11
	NIII/NII at 25000 Kelvin 0.0017600719525

Problem 8.10c code results from Saha2()

	Enter temperature:   15700000
	Enter Z1:   2
	Enter Z2:   1
	Enter Energy (in eV):   10.2
	The fraction of ionized H is 0.709643283426 
"""
