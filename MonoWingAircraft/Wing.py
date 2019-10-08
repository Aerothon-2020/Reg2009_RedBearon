from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import LBF, SEC, ARCDEG, FT, IN, SLUG
from scalar.units import AsUnit
from Aerothon.ACWing import ACMainWing
from Aerothon.DefaultMaterialsLibrary import PinkFoam, Monokote, Basswood, Balsa
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing

#
# Create the wing
#
Wing = ACMainWing(1)
Wing.Lift_LO       = 35 * LBF
Wing.V_max_climb   = 65 * FT/SEC
Wing.V_Stall       = 35 * FT/SEC
Wing.Alt_LO        = 920 * FT
#Wing.AR            = 5.0
Wing.b             = 95*IN


###############################################################################
#
# Geometric properties
#
###############################################################################

Wing.FullWing = True

#Wing.UpperWing.b   = 4.5*FT
#Wing.LowerWing.b   = 4*FT

Wing.TR      = [1,0.85,1]
Wing.Gam     = [0*ARCDEG, 0*ARCDEG, 0*ARCDEG]
Wing.Lam     = [0*ARCDEG, 0*ARCDEG, 0*ARCDEG]
Wing.Fb      = [0.5,0.9,1]
Wing.CEdge   = 'LE'
Wing.ConstUpper = True

###############################################################################
#
# Aerodynamic properties
#
###############################################################################


#
# Set the airfoils
#
Wing.Airfoil = 'e423'

Wing.o_eff = 0.98
Wing.FWCF = 0.98


#
# Polar slope evaluations
#

Wing.ClSlopeAt = (6*ARCDEG, 7*ARCDEG)
Wing.CmSlopeAt = (-1*ARCDEG, 0*ARCDEG)

###############################################################################
#
# Control surfaces
#
###############################################################################

#
# Define the control surfaces
#
Wing.AddControl('Aileron')
Wing.Aileron.Fc = 0.25
Wing.Aileron.Fb = 0.4
Wing.Aileron.Ft = 0.1
Wing.Aileron.SgnDup = -1.

Wing.Aileron.Servo.Fc     = 0.3
Wing.Aileron.Servo.Weight = 0.01*LBF

###############################################################################
#
# Structural properties
#
###############################################################################
#
# Spar material (basswood, 1/4in width at max airfoil thickness + d-spar skin, balsa 1/16in)
#
sparw = 0.25*IN
Basswood = Basswood.copy()
Balsa    = Balsa.copy()
Wing.Refresh() # refresh so the thicknesses can be calculated
Wthick  = Wing.Thickness(0*FT)
sparFD  = Basswood.ForceDensity * sparw * Wthick

# Dspar density as balsa at 1/16in thick and the distance around the front of the airfoil
#  approximated as 2 times the airfoil thickness at the root
DsparFD = Balsa.ForceDensity * 0.0625*IN * 2.0 * Wthick

#
# Rib material (1/8in balsa)
#
BWRibMat = Balsa.copy()
BWRibMat.Thickness = 0.125*IN

Wing.SetWeightCalc(ACRibWing)
Wing.WingWeight.SkinMat                    = Monokote.copy()
Wing.WingWeight.RibMat                     = BWRibMat
Wing.WingWeight.RibSpace                   = 5*IN

#Wing.SetWeightCalc(ACSolidWing)
#Wing.WingWeight.SparMat.LinearForceDensity = 0.0051*LBF/IN
#Wing.WingWeight.SkinMat                    = Monokote.copy()
#Wing.WingWeight.WingMat                    = PinkFoam.copy()
#Wing.WingWeight.WingMat.ForceDensity      *= 0.5

if __name__ == '__main__':
    import pylab as pyl
    
    print "V lift of   : ", AsUnit( Wing.GetV_LO(), 'ft/s' )
    print "V stall     : ", AsUnit( Wing.V_Stall, 'ft/s' )
    print "Wing Area   : ", AsUnit( Wing.S, 'in**2' )
    print "Wing Span   : ", AsUnit( Wing.b, 'ft' )
    print "Wing AR     : ", Wing.AR
    print "Wing MAC    : ", AsUnit( Wing.MAC(), 'in' )
    print "Wing Xac    : ", Wing.Xac()
    print "Wing dCM_da : ", Wing.dCM_da()
    print "Wing dCL_da : ", Wing.dCL_da()
    print "Lift of Load: ", AsUnit( Wing.Lift_LO, 'lbf' )

    print "Wing Thickness: ", Wing.Thickness(0*FT)
    print "Wing Chord    : ", Wing.Chord(0*FT)
    print "Wing Area     : ", Wing.S
    print "Wing Lift     : ", Wing.Lift_LO
    print
    print "Wing Weight : ", AsUnit( Wing.Weight, 'lbf' )
    print "Wing MOI    : ", AsUnit( Wing.MOI(), 'slug*ft**2' )
   
    Wing.WriteAVLWing('MonoWing.avl')
    
#    Wing.Draw3DWingPolars(fig=5)
#    Wing.Draw2DAirfoilPolars(fig=4)
#    
#    Wing.Draw3DWingPolars(fig=3)
#    Wing.Draw2DAirfoilPolars(fig=2)

    Wing.Draw(fig = 1)
    pyl.show()