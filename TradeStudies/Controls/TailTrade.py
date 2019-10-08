from Aerothon.ACControls import ACControls
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
from scalar.units import SEC, ARCDEG
import pylab as pyl
import numpy as npy

Execute = True
#
# Do a trade study on horizontal tail volume coefficient
#
HTail = Aircraft.HTail
Controls = ACControls(Aircraft)

Controls.RunDir = 'AVLControls/'

#
# The length must be specified for the ACLenAircraft restriction
# to perform correctly, so make sure the area is not specified.
#
if HTail.S is not None:
    HTail.S = None
    
VCs = npy.linspace(0.3,0.5,5)

for i in range(len(VCs)):
    run = 'Run' + str(i)
    HTail.VC = VCs[i]
    Controls.AddRun(run,'AVLAircraft' + str(i) + '.avl', WriteAVLInput = Execute)
    Controls.Runs[i].DumpStability('STFile' + str(i) + '.txt')


if Execute:
    Controls.ExecuteAVL()

Controls.ReadAVLFiles()

PDamp = npy.empty(len(VCs))

t = npy.linspace(0,5)*SEC

legend = []
for i in range(len(VCs)):
    HTail.VC = VCs[i]
    Controls.SetToAircraft()
 #   Controls.Deriv[i].StabilityTable(i+2)
    PDamp[i] = Controls.Deriv[i].PitchDamp()
    
    Controls.Deriv[i].PlotPitchResponseDueToElevator(3 * ARCDEG, t, 'Elevator', 1)
    legend.append('VC = %1.2f' % VCs[i])


pyl.figure(len(VCs) + 2)
pyl.plot(VCs, PDamp)
pyl.xlabel('Horizontal Tail VC')
pyl.ylabel('Pitch Damping Coefficient')
pyl.axhline(y = 1, color = 'k')

pyl.figure(1)
pyl.legend(legend, loc = 'best')

pyl.show()
