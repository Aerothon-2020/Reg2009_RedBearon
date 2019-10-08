from Aerothon.ACControls import ACControls
from Aircraft_Models.Reg2009Aircraft_RedBearon.MonoWingAircraft.Aircraft import Aircraft
from scalar.units import IN, LBF, ARCDEG, SEC
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy

#
# Set-up AVL Controls Run
#
Controls = ACControls(Aircraft)
Controls.RunDir = 'AVLControls/'
Controls.AddRun('Stab', 'AVLAircraft.avl', WriteAVLInput = True)
Controls.Stab.DumpStability('AVLDeriv.txt')
Controls.Stab.Exit()

Controls.ExecuteAVL()

Controls.ReadAVLFiles()

Deriv = Controls.Deriv[0]

Deriv.StabilityTable(fig=1)

print
print
print "Aircraft MOI          : ", Aircraft.MOI()
print 'Steady state roll rate: ', AsUnit( Deriv.RollDueToAileron(15 * ARCDEG, 'Aileron'), 'deg/s')
print 'Steady state pitch rate: ', Deriv.PitchResponseDueToElevator(15 * ARCDEG, 1*SEC, 'Elevator')

Aircraft.Draw(2)
pyl.show()