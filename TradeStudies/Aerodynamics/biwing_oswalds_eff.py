from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG
#from Aerothon.ACWing import ACBiWing
import pylab as pyl
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing as biwing

RunDir = 'biwing_gap_vs_oeff/'

biwing.Stagger = -1.0

##DO NOT specify an Fb of 1 for the end plate!!!
##An Fb of 1 is at the Upper Wing and does not need to be specified
biwing.EndPlate.Fb        = [0.2,0.5,0.8]
biwing.EndPlate.TR        = [1,1,1]
biwing.EndPlate.Gam       = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
biwing.EndPlate.Lam       = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
biwing.EndPlate.Symmetric = True
biwing.EndPlate.CEdge     = 'LE'

biwing.Gap = 0.1
e1 = biwing.GetAVLOswald('AVLBiWing0.1.avl', RunDir, True)
biwing.Draw(1)

biwing.Gap = 0.2
e2 = biwing.GetAVLOswald('AVLBiWing0.2.avl', RunDir, True)
biwing.Draw(2)

biwing.Gap = 0.3
e3 = biwing.GetAVLOswald('AVLBiWing0.3.avl', RunDir, True)
biwing.Draw(3)

biwing.Gap = 0.4
e4 = biwing.GetAVLOswald('AVLBiWing0.4.avl', RunDir, True)

biwing.Draw(4)

print
print 'Oswald effeciency, Gap = 0.1 = ', e1
print 'Oswald effeciency, Gap = 0.2 = ', e2
print 'Oswald effeciency, Gap = 0.3 = ', e3
print 'Oswald effeciency, Gap = 0.4 = ', e4


pyl.show()