from Aerothon.ACControls import ACControls
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
from scalar.units import IN, LBF, ARCDEG, SEC
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import cmath as math

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
print 'Steady state roll rate: ', AsUnit(Deriv.RollDueToAileron(15 * ARCDEG, 'Aileron'), 'deg/s')
print 'Steady state pitch rate: ', Deriv.PitchResponseDueToElevator(25 * ARCDEG, 1*SEC, 'Elevator')*180/math.pi
print
print 'Yb = ', Deriv.Yb()
print 'Yr = ', Deriv.Yr()
print 'Nb = ', Deriv.Nb()
print 'Nr = ', Deriv.Nr()
print 'Np = ', Deriv.Np()
print 'Lb = ', Deriv.Lb()
print 'Lr = ', Deriv.Lr()
print 'Ma = ', Deriv.Ma()
print 'Mq = ', Deriv.Mq()
print 'Za = ', Deriv.Za()
print 'Xu = ', Deriv.Xu()
print 'Ndc = ', Deriv.Ndc(3 * ARCDEG ,'Aileron')
print 'Ldc = ', Deriv.Ldc(3 * ARCDEG ,'Aileron')
print 'Pdc = ', Deriv.Pdc(3 * ARCDEG ,'Rudder')
print
print 'Dutch Roll Freq: ', Deriv.DutchRollFreq()
print 'Dutch Roll Damp: ', Deriv.DutchRollDamp()    
print
print 'Short Period Freq: ', Deriv.ShortPeriodFreq()
print 'Short Period Damp: ', Deriv.ShortPeriodDamp()
print
print 'Long Period Freq: ', Deriv.LongPeriodFreq()
print 'Long Period Damp: ', Deriv.LongPeriodDamp()    
print
print 'Spiral Mode: ', Deriv.SpiralMode()
print 'Spiral double time: ', Deriv.SpiralDoubleTime()
print
print 'Pitch Freq: ', Deriv.PitchFreq()
print 'Pitch Damp: ', Deriv.PitchDamp()
print 'Pitch Phase Ang: ', Deriv.PitchPhaseAng()
print 'Pitch Double Time: ', Deriv.PitchDoubleTime()
print
print 'Madot = ', Deriv.Madot()
print 'Zq = ', Deriv.Zq()
print 'Liftoff Velocity = ', Controls.u0
print 'Reference 2d aoa =', Controls.Alpha2d
print 'Current Altitude =', Controls.Alt

Aircraft.Draw(2)
pyl.show()