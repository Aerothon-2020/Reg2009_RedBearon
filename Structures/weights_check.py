from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import LBF, IN, OZF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

#
# Use this file to check the model weights to built test sections
###############################################################################

print '##########################################'
print 'Aircraft Weights'
print '##########################################'
print
print 'Empty   Weight     : ', AsUnit( Aircraft.EmptyWeight, 'lbf' )
print
print 'Engine Weight      : ', AsUnit( Aircraft.Propulsion.Weight, 'lbf' )
print
print 'Nose Gear Weight   : ', AsUnit( Aircraft.NoseGear.Weight, 'lbf' )
print 'Main Gear Weight   : ', AsUnit( Aircraft.MainGear.Weight, 'lbf' )
print
print 'Wing  Weight       : ', AsUnit( Aircraft.Wing.Weight, 'lbf' )
print '  Upper Wing       : ', AsUnit( Aircraft.Wing.UpperWing.Weight, 'lbf' )
print '  Lower Wing       : ', AsUnit( Aircraft.Wing.LowerWing.Weight, 'lbf' )
print '  Endplate         : ', AsUnit( Aircraft.Wing.EndPlate.Weight, 'lbf' )
print
print 'Horiz Weight       : ', AsUnit( Aircraft.HTail.Weight, 'lbf' )
print 'Vert  Weight       : ', AsUnit( Aircraft.VTail.Weight, 'lbf' )
print
print 'Fuselage Weight    : ', AsUnit( Aircraft.Fuselage.Weight, 'lbf' )
print '  Nose Weight      : ', AsUnit( Aircraft.Fuselage.Nose.Weight, 'lbf' )
print '  PyldBay  Weight  : ', AsUnit( Aircraft.Fuselage.PyldBay.Weight, 'lbf' )
print '  TailTaper Weight : ', AsUnit( Aircraft.Fuselage.TailTaper.Weight, 'lbf' )
print
print




Fuse = Aircraft.Fuselage

# Fuselage tail taper section
#-----------------------------------------------------------------------------#
# Built test section: 31.5 in, 4.09 oz
# Supported 4lbf at the end of the test section with a 36lbf-in torques
test  = ((4.09)*OZF/(31.5*IN)) / (OZF/IN)
model = (Fuse.TailTaper.Weight/Fuse.TailTaper.Length) / (OZF/IN)

print '##########################################'
print 'Weight Check'
print '##########################################'
print
print 'Tail taper section linear force density'
print 'Test section: %(1)5.4f OZF/IN     Model: %(2)5.4f OZF/IN' % {'1':test,'2':model} 
print


# Wing Weight
#-----------------------------------------------------------------------------#
# Built test section: 36 in, 0.7 lbf
# Approximate wing weight of 1.75 lbf
test  = 1.75
model = Aircraft.Wing.UpperWing.Weight / (LBF)

print 'Wing weight'
print 'Test section: %(1)4.3f LBF         Model: %(2)4.3f LBF' % {'1':test,'2':model}
print

