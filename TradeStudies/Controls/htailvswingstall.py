from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import ARCDEG
import numpy as npy
import pylab as pyl
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

HTail = Aircraft.HTail
Wing  = Aircraft.Wing

Alpha1 = Wing.AlphaRange()                       #2D angle of attack
Alpha = (Wing.AlphaFus(Alpha1)) / ARCDEG #Fuselage angle of attack

del_e = Aircraft.del_e_trim(Alpha1)

CLh1 = HTail.CL(Alpha1, del_e = 0*ARCDEG)
CLh2 = HTail.CL(Alpha1, del_e = 10*ARCDEG)
CLh3 = HTail.CL(Alpha1, del_e = -10*ARCDEG)
CLh4 = HTail.CL(Alpha1, del_e = del_e)
CLw = Wing.CL(Alpha1)

pyl.figure(1)
pyl.plot(Alpha,CLh1,'r',Alpha,CLh2,'g',Alpha,CLh3,'b',Alpha,CLh4,'m',Alpha,CLw,'k')
pyl.xlabel(r'$\alpha$')
pyl.ylabel(r'$C_L$')

pyl.legend(['HTail del_e=0','HTail del_e=10','HTail del_e=-10','HTail del_e=del_e trim','Wing'],loc='best')

pyl.show()