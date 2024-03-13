import numpy as np
import matplotlib.pyplot as mpl
import lvm_read as lvm
from scipy.optimize import curve_fit

#données = getLvmData_dict("Labview partie 4_1.lvm")

donéesPartc = []
for i in range(6,16):
    données = lvm.read(f"Données Labview/Donnèes Partie1_{i}.lvm")[0]['data']
    unitéx = []
    unitéy = []
    for donnée in données:
        unitéx.append(donnée[0])
        unitéy.append(donnée[1])
    donéesPartc.append([unitéx, unitéy])

donéesPartf = []
for i in range(1,11):
    données = lvm.read(f"Données Labview/Donnèes Partie1f_{i}.lvm")[0]['data']
    unitéx = []
    unitéy = []
    for donnée in données:
        unitéx.append(donnée[0])
        unitéy.append(donnée[1])
    donéesPartf.append([unitéx, unitéy])


moyennesc = [[],[]]
moyennesf = [[],[]]



for donnée in donéesPartc:
    moyennesc[1].append(np.mean(donnée[0]))
    moyennesc[0].append(np.mean(donnée[1]))

for donnée in donéesPartf:
    moyennesf[1].append(np.mean(donnée[0]))
    moyennesf[0].append(np.mean(donnée[1]))


def PuissanceC(R, Rs, Xs):
    return np.divide(R, np.add(np.multiply(np.add(R,Rs),np.add(R,Rs)), np.multiply(Xs,Xs)))/2


Xc = -1 / (2*np.pi*4*1000*10**(-6))
print(Xc)
scale=1
puissancesc = []
for i in range(10):
    puissancesc.append(moyennesc[1][i]*moyennesc[1][i]/moyennesc[0][i])
puissancesf = []
for i in range(10):
    puissancesf.append(moyennesf[1][i]*moyennesf[1][i]/moyennesf[0][i])

fitC = curve_fit(PuissanceC, moyennesc[0], puissancesc)


Rsfit = fitC[0][0]
Xsfit = fitC[0][1]


def PuissanceF(R, Rs, Xs):
    return np.divide(R, np.add(np.multiply(R+Rs,R+Rs), np.multiply((Xs),(Xs))))/2

fitF = curve_fit(PuissanceF, moyennesf[0], puissancesf)
print(fitF[0])
print(fitC[0])

fig, ax1 = mpl.subplots()

ax1.set_xlabel("Résistance")
ax1.set_ylabel('Puissance')
#ax1.set_xscale("log")
ax1.plot(moyennesc[0], puissancesc, "-k")
ax1.plot(moyennesc[0], puissancesc, ".r")
ax1.plot(np.linspace(1,200,200), PuissanceC(np.linspace(1,200,200), fitC[0][0], fitC[0][1]), "-g")
ax1.plot(moyennesf[0], puissancesf, "-b")
ax1.plot(moyennesf[0], puissancesf, ".r")
ax1.plot(np.linspace(1,200,200), PuissanceF(np.linspace(1,200,200), fitF[0][0], fitF[0][1]), "-g")
ax1.tick_params(axis='y')

mpl.show()

