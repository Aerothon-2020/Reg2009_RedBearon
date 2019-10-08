from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import LBF, SEC, ARCDEG, FT, IN, SLUG, OZF
from scalar.units import AsUnit
from Aerothon.ACWing import ACBiWing
from Aerothon.DefaultMaterialsLibrary import PinkFoam, Monokote, Balsa
from Aircraft_Models.Reg2009Aircraft_RedBearon.Materials.Mats import BWRibMat, UDsparFD, LDsparFD, UsparFD, LsparFD
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing

#
# Create the wing
#
BoxWing = ACBiWing(1, 4, 5)
BoxWing.name          = 'Box Wing'
BoxWing.Lift_LO       = 37 * LBF
BoxWing.Lift_Ratio    = 0.5
BoxWing.V_max_climb   = 65 * FT/SEC
BoxWing.V_Stall       = 33.75 * FT/SEC
BoxWing.Alt_LO        = 920 * FT


###############################################################################
#
# Geometric properties
#
###############################################################################

BoxWing.FullWing = True

BoxWing.Gap        = 0.3
BoxWing.Stagger    = 0.2

BoxWing.b             = 82*IN
#BoxWing.UpperWing.b   = 4.5*FT
#BoxWing.LowerWing.b   = 4*FT

BoxWing.LowerWing.TR      = [1,1]
BoxWing.LowerWing.Gam     = [0*ARCDEG, 0*ARCDEG]
BoxWing.LowerWing.Lam     = [0*ARCDEG, 0*ARCDEG]
BoxWing.LowerWing.Fb      = [0.6,1]

BoxWing.UpperWing.TR      = [1,1]
BoxWing.UpperWing.Gam     = [0*ARCDEG, 0*ARCDEG]
BoxWing.UpperWing.Lam     = [0*ARCDEG, 0*ARCDEG]
BoxWing.UpperWing.Fb      = [0.6,1]

#
# Turn off detailed drawing for the wings
#
BoxWing.UpperWing.DrawDetail = False
BoxWing.LowerWing.DrawDetail = False

#
# Create and Endplate 
#
BoxWing.CreateEndPlate()

#
# DO NOT specify an Fb of 1 for the end plate!!!
# An Fb of 1 is at the Upper Wing and does not need to be specified
#
BoxWing.EndPlate.Fb      = [0.02,0.5,0.98]
BoxWing.EndPlate.TR      = [0.8,0.5,2.0]
BoxWing.EndPlate.Gam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
BoxWing.EndPlate.Lam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
BoxWing.EndPlate.Symmetric = True
BoxWing.EndPlate.CEdge   = 'TE'


###############################################################################
#
# Aerodynamic properties
#
###############################################################################


#
# Set the airfoils
#
BoxWing.UpperWing.Airfoil = 'e423'
BoxWing.LowerWing.Airfoil = 'e423'
BoxWing.EndPlate.Airfoil =  'NACA0012'

#
# Set up the variation of Oswald efficiency vs. gap
#
BoxWing.GapInterp  = [0.1   ,0.2   ,0.3   ,0.4]
BoxWing.OeffInterp = [1.1832,1.3371,1.4617,1.5676]

#
# Determine the correct Biwing correction factor for the given wing
# TODO: Correct BWCFInterp
#
BoxWing.BWCFInterp     = [0.69,0.785,0.835,0.87]
BoxWing.LowerWing.FWCF = 1 
BoxWing.UpperWing.FWCF = 1

#
# Polar slope evaluations
#
BoxWing.ClSlopeAt = (0*ARCDEG, 1*ARCDEG)
BoxWing.CmSlopeAt = (0*ARCDEG, 1*ARCDEG)

BoxWing.LowerWing.ClSlopeAt = (6*ARCDEG, 7*ARCDEG)
BoxWing.LowerWing.CmSlopeAt = (-1*ARCDEG, 0*ARCDEG)

BoxWing.UpperWing.ClSlopeAt = BoxWing.LowerWing.ClSlopeAt
BoxWing.UpperWing.CmSlopeAt = BoxWing.LowerWing.CmSlopeAt

###############################################################################
#
# Control surfaces
#
###############################################################################

#
# Define the control surfaces
#
BoxWing.LowerWing.AddControl('Aileron')
BoxWing.LowerWing.Aileron.Fc = 0.25
BoxWing.LowerWing.Aileron.Fb = 0.40
BoxWing.LowerWing.Aileron.Ft = 0.10
BoxWing.LowerWing.Aileron.SgnDup = -1.

BoxWing.LowerWing.Aileron.Servo.Fc     = 0.3
BoxWing.LowerWing.Aileron.Servo.Weight = 0.77*OZF

###############################################################################
#
# Structural properties
#
###############################################################################
#Lower Wing
BoxWing.LowerWing.SetWeightCalc(ACRibWing)
BoxWing.LowerWing.WingWeight.AddSpar("MainSpar",1.307*IN,1*IN)
BoxWing.LowerWing.WingWeight.MainSpar.SparMat = Balsa.copy()
#BoxWing.LowerWing.WingWeight.SparMat.LinearForceDensity = LsparFD + LDsparFD
BoxWing.LowerWing.WingWeight.SkinMat                    = Monokote.copy()
BoxWing.LowerWing.WingWeight.RibMat                     = BWRibMat
BoxWing.LowerWing.WingWeight.RibSpace                   = 4*IN
BoxWing.LowerWing.WingWeight.DrawDetail = True

#Upper Wing
BoxWing.UpperWing.SetWeightCalc(ACRibWing)
BoxWing.UpperWing.WingWeight.AddSpar("MainSpar",1.307*IN,1*IN)
BoxWing.UpperWing.WingWeight.MainSpar.SparMat = Balsa.copy()
#BoxWing.UpperWing.WingWeight.SparMat.LinearForceDensity = UsparFD + UDsparFD
BoxWing.UpperWing.WingWeight.SkinMat                    = Monokote.copy()
BoxWing.UpperWing.WingWeight.RibMat                     = BWRibMat
BoxWing.UpperWing.WingWeight.RibSpace                   = 4*IN
BoxWing.UpperWing.WingWeight.DrawDetail = True

#End Plate
BoxWing.EndPlate.SetWeightCalc(ACSolidWing)
BoxWing.EndPlate.WingWeight.AddSpar("MainSpar", 0.25*IN, 0.25*IN)
BoxWing.EndPlate.WingWeight.MainSpar.SparMat = Balsa.copy()
#BoxWing.EndPlate.WingWeight.SparMat.LinearForceDensity = 0.0025*LBF/IN
BoxWing.EndPlate.WingWeight.SkinMat                    = Monokote.copy()
BoxWing.EndPlate.WingWeight.WingMat                    = PinkFoam.copy()
BoxWing.EndPlate.WingWeight.WingMat.ForceDensity      *= 0.6


if __name__ == '__main__':
    import pylab as pyl
    
    print "V lift of   : ", AsUnit( BoxWing.GetV_LO(), "ft/s" )
    print "V stall     : ", AsUnit( BoxWing.V_Stall, "ft/s" )
    print "Wing Area   : ", AsUnit( BoxWing.S, "in**2" )
    print "Wing Span   : ", AsUnit( BoxWing.b, "ft" )
    print "Wing AR     : ", BoxWing.AR
    print "Wing MAC    : ", AsUnit( BoxWing.MAC(), "in" )
    print "Wing Xac    : ", AsUnit( BoxWing.Xac(), "in" )
    print "Wing dCM_da : ", BoxWing.dCM_da()
    print "Wing dCL_da : ", BoxWing.dCL_da()
    print "Lift of Load: ", AsUnit( BoxWing.Lift_LO, "lbf" )
    print "Wing BWFC   : ", BoxWing.BWCF()
    print
    print "Wing Thickness: ", BoxWing.LowerWing.Thickness(0*FT)
    print "Wing Chord    : ", BoxWing.LowerWing.Chord(0*FT)
    print "LowerWing Area: ", BoxWing.LowerWing.S
    print "UpperWing Area: ", BoxWing.UpperWing.S
    print "LowerWing lift: ", BoxWing.LowerWing.Lift_LO
    print "UpperWing lift: ", BoxWing.UpperWing.Lift_LO
    print
    print "Wing Weight : ", AsUnit( BoxWing.Weight, "lbf" )
    print "Wing MOI    : ", AsUnit( BoxWing.MOI(), "slug*ft**2" )
    print "LowerWing Weight : ", AsUnit( BoxWing.LowerWing.Weight, "lbf" )
    print "UpperWing Weight : ", AsUnit( BoxWing.UpperWing.Weight, "lbf" )
    print "EndPlate Weight  : ", AsUnit( BoxWing.EndPlate.Weight, "lbf" )
    print "EndPlate Area    : ", AsUnit( BoxWing.EndPlate.S, "in**2" )
    
    BoxWing.WriteAVLWing('AVLControls/BoxWing.avl')
    
#    BoxWing.LowerWing.Draw3DWingPolars(fig=7)
#    BoxWing.LowerWing.Draw2DAirfoilPolars(fig=6)
#
#    BoxWing.UpperWing.Draw3DWingPolars(fig=5)
#    BoxWing.UpperWing.Draw2DAirfoilPolars(fig=4)
#    
    BoxWing.Draw3DWingPolars(fig=3)
    BoxWing.Draw2DAirfoilPolars(fig=2)

    
    BoxWing.LowerWing.WingWeight.DrawRibs = True
    BoxWing.LowerWing.WingWeight.Draw(fig=1)
    BoxWing.UpperWing.WingWeight.Draw(fig=1)

    BoxWing.Draw(fig = 1)
    pyl.show()