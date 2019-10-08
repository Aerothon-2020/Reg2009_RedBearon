from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ
#_environ["scalar_off"] = "off"

from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG, SLUG, MIN, OZF
from scalar.units import AsUnit
from Aerothon.ACBase import g
from Aerothon.ACAircraft import ACTailAircraft
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum
from Fuselage import Fuselage
from Aircraft_Models.Reg2009Aircraft_RedBearon.Propulsion.Propulsion import Propulsion
from BiWing import BoxWing
import pylab as pyl
import cmath as math
from Aerothon.ACTLenAircraft import ACTLenAircraft

#
# Create the Aircraft from the ACTLenAircraft class, which limits the sum of the L,W,and H
#
Aircraft = ACTLenAircraft()
Aircraft.name = 'AeroCats_2008_BoxPlane'

#
# The total allowable lengths summing height + width + length of the aircraft
#
Aircraft.TotalLengths = 174*IN

# 
# Assign the already generated parts
#
Aircraft.SetFuselage(Fuselage)
Aircraft.SetPropulsion(Propulsion)
Aircraft.SetWing(BoxWing)

#
# Position the wing on the bottom of the fuselage
#
Aircraft.WingFuseFrac = -0.32

#
# Aircraft Properties
#
Aircraft.TotalWeight = 32*LBF

#Add Payload for check of balance
#Fuselage.PyldBay.AddComponent   ("Payload", 23.0*LBF , (4.25*IN,4.75*IN,4.5*IN) , "Bottom"  , (0.3 , 0.5, 0.5) )

Aircraft.TippingAngle     = 10*ARCDEG
Aircraft.RotationAngle    = 15*ARCDEG
Aircraft.Alpha_Groundroll = 0*ARCDEG

Aircraft.CMSlopeAt   = (0 * ARCDEG, 15 * ARCDEG)
Aircraft.CLSlopeAt   = (6 * ARCDEG, 7 * ARCDEG)
Aircraft.CLHTSlopeAt = (8 * ARCDEG, 9 * ARCDEG) 
Aircraft.DWSlopeAt   = (7 * ARCDEG, 8 * ARCDEG)

Aircraft.Alpha_Zero_CM  = 8 * ARCDEG
Aircraft.StaticMargin   = 0.1

#
# Maximum velocity for plotting purposes
#
Aircraft.VmaxPlt = 70*FT/SEC

#
# Estimate for the time the aircraft rotates on the ground during takeoff
#
Aircraft.RotationTime = 0.1 * SEC

#
# Rolling friction
#
Aircraft.Mu_r = 0.04


###############################################################################
#
# Tail surfaces
#
###############################################################################

#==============================================================================
# Horizontal tail
#
HTail = Aircraft.HTail
#HTail.Airfoil  = ('NACA0012/NACA1410.dat','NACA1410')
HTail.Airfoil  = 'NACA0012'
#HTail.Airfoil  = ('clarky/clarky.dat','clarky')
#HTail.Airfoil  = ('e423/e423.dat','e423')
HTail.AR       = 3.85
HTail.TR       = 0.6
#HTail.S        = 200 * IN**2
HTail.L        = 100 * IN
#HTail.VC       = 0.3842
HTail.VC       = 0.42
HTail.FullWing = True
HTail.DWF      = 2.0 #Main wing Down wash factor (Between 1.0 and 2.0)
HTail.Inverted = True

#
# Elevator properties
#
HTail.Elevator.Fc = 0.3
HTail.Elevator.Fb = 1.0
HTail.Elevator.Ft = 0.0

HTail.Elevator.Servo.Fc  = 0.4
HTail.Elevator.Servo.Fbc = 0.0
HTail.Elevator.Servo.Weight = 0.77*OZF

#Set the sweep about the elevator hinge
HTail.SweepFc  = 1.0 - HTail.Elevator.Fc

#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
Basswood = Basswood.copy()
Balsa    = Balsa.copy()
BWRibMat = Balsa.copy()
BWRibMat.Thickness = 0.125 * IN

HTail.SetWeightCalc(ACRibWing)
HTail.WingWeight.RibMat                    = BWRibMat
HTail.WingWeight.RibSpace                  = 3 * IN
#HTail.SetWeightCalc(ACSolidWing)
#HTail.WingWeight.WingMat                    = PinkFoam.copy()
#HTail.WingWeight.WingMat.ForceDensity      *= 0.4

HTail.WingWeight.AddSpar("HMainSpar",0.25*IN,0.5*IN)
HTail.WingWeight.HMainSpar.SparMat = Balsa.copy()
HTail.WingWeight.SkinMat                    = Monokote.copy()
HTail.WingWeight.DrawDetail = True

#==============================================================================
# Vertical tail
#
VTail = Aircraft.VTail
VTail.Airfoil = 'NACA0012'
VTail.VC      = 0.0325
VTail.AR      = 2
VTail.TR      = 0.7
VTail.Axis    = (0, 1)
VTail.L       = 100.0 * IN
#VTail.S       = 100 * IN**2
#VTail.b       = 10 * IN

#
# Rudder properties
#
VTail.Rudder.Fc = 0.4
VTail.Rudder.Servo.Fc  = 0.3
VTail.Rudder.Servo.Fbc = 0.1
VTail.Rudder.Servo.Weight = 0.77*OZF

#Set the sweep about the rudder hinge
VTail.SweepFc = 1.0 - VTail.Rudder.Fc

#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
VTail.SetWeightCalc(ACRibWing)
VTail.WingWeight.RibMat                    = BWRibMat
VTail.WingWeight.RibSpace                  = 3 * IN
#VTail.SetWeightCalc(ACSolidWing)
#VTail.WingWeight.WingMat                    = PinkFoam.copy()
#VTail.WingWeight.WingMat.ForceDensity      *= 0.4

VTail.WingWeight.AddSpar("VMainSpar",0.25*IN,0.5*IN)
VTail.WingWeight.VMainSpar.SparMat = Balsa.copy()
VTail.WingWeight.SkinMat                    = Monokote.copy()
VTail.WingWeight.DrawDetail = True


###############################################################################
#
# Landing Gear
#
###############################################################################
Steel = Steel.copy()
MainGear = Aircraft.MainGear
MainGear.Theta        = 55*ARCDEG
MainGear.GearHeight   = 8   * IN
MainGear.StrutW       = 0.2 * IN
MainGear.StrutH       = 0.1 * IN
MainGear.WheelDiam    = 2.5 * IN
MainGear.X[1]         = 2.5 * IN
MainGear.Strut.Weight = 0.3*LBF
#MainGear.Strut.Weight = math.pi*(0.125/2*IN)**2*12*IN*Steel.ForceDensity #1/8 inch diameter steel, l=12in
MainGear.Wheel.Weight = 0.1*LBF

NoseGear = Aircraft.NoseGear
NoseGear.StrutW    = 0.1 * IN
NoseGear.StrutH    = 0.1 * IN
NoseGear.WheelDiam = 2.5 * IN
NoseGear.Strut.Weight =0.2*LBF 
#NoseGear.Strut.Weight = math.pi*(0.125/2*IN)**2*8*IN*Steel.ForceDensity #1/8 inch diameter steel, l=8in
NoseGear.Wheel.Weight = 0.1*LBF

#if __name__ == '__main__':
def real_main():
    
    TCG = Aircraft.CG()
    ACG = Aircraft.Fuselage.AircraftCG()
    dCG = TCG - ACG
    
    print 'Aircraft Xnp   :', Aircraft.Xnp()
    print 'Aircraft Xcg   :', Aircraft.Xcg()
    print 'Aircraft CM    :', Aircraft.CM(15*ARCDEG, del_e = 10*ARCDEG)
    print 'Aircraft dCM_da:', Aircraft.dCM_da()
    print
    print 'Wing Area      :', AsUnit( Aircraft.Wing.S, 'in**2' )
    print 'Wing MAC       :', AsUnit( Aircraft.Wing.MAC(), 'in' )
    print 'Wing dCl_da    :', AsUnit( Aircraft.Wing.dCL_da(), '1/rad' )
    print 'Wing Xac       :', AsUnit( Aircraft.Wing.Xac(), 'in' )
    print 'Wing Downwash  :', Aircraft.WingDownWash(0*ARCDEG)
    print 'Wing Separation: ', Aircraft.Wing.UpperWing.X[2] - Aircraft.Wing.LowerWing.X[2]
    print 'Wing Stagger   : ', Aircraft.Wing.UpperWing.X[0] - Aircraft.Wing.LowerWing.X[0]
    print
    print 'Horiz Area     :', AsUnit( Aircraft.HTail.S, 'in**2' )
    print 'Horiz Span     :', AsUnit( Aircraft.HTail.b, 'in' )
    print 'Horiz Root     :', Aircraft.HTail.Chord(0*IN)
    print 'Horiz Tip      :', Aircraft.HTail.Chord(Aircraft.HTail.b/2)
    print 'Horiz Tip Swp  :', Aircraft.HTail.LE(Aircraft.HTail.b/2)-Aircraft.HTail.LE(0*IN)
    print 'Horiz VC       :', Aircraft.HTail.VC
    print 'Horiz Dsgn CL  :', Aircraft.GetHT_Design_CL()
    print 'Horiz Inc      :', Aircraft.HTail.i
    print 'Horiz dCl_da   :', AsUnit( Aircraft.HTail.dCL_da(), '1/rad' )
    print
    print 'Vert Area      :', AsUnit( Aircraft.VTail.S, 'in**2' )
    print 'Vert Span      :', AsUnit( Aircraft.VTail.b, 'in' )
    print 'Vert Root      :', Aircraft.VTail.Chord(0*IN)
    print 'Vert Tip       :', Aircraft.VTail.Chord(Aircraft.VTail.b)
    print 'Vert Tip Swp   :', Aircraft.VTail.LE(Aircraft.VTail.b)-Aircraft.VTail.LE(0*IN)
    print 'Vert VC        :', Aircraft.VTail.VC
    print
    print 'True CG        :', TCG[0]
    print 'Desired CG     :', ACG[0]
    print 'CG Loc rel Wing:', ACG[0]-Aircraft.Wing.LowerWing.LE(0*IN)
    print 'NP Loc rel Wing:', AsUnit( Aircraft.Xnp() - Aircraft.Wing.LowerWing.LE(0*IN), 'in' )
    print 'delta CG       :', dCG[0]
    print 'Empty   Weight :', AsUnit( Aircraft.EmptyWeight, 'lbf' )
    print 'Payload Weight :', AsUnit( Aircraft.PayloadWeight(), 'lbf' )
    print
    print 'Composite Nose'
    Nose = Aircraft.Fuselage.Nose
    CompWeight = Nose.Weight + Nose.FrontBulk.Weight + Nose.BackBulk.Weight
    print '  Composite Nose Weight: ', AsUnit( CompWeight, 'lbf' )
    print '  Composite Nose Area: ', AsUnit( ((CompWeight / Nose.SkinMat.AreaDensity)/g), 'in**2' )
    print '  Composite Nose Density: ', AsUnit( Nose.SkinMat.AreaDensity*g, 'lbf/in**2' )
    print
    print 'Wing  Weight   :', AsUnit( Aircraft.Wing.Weight, 'lbf' )
    print 'Horiz Weight   :', AsUnit( Aircraft.HTail.Weight, 'lbf' )
    print 'Vert  Weight   :', AsUnit( Aircraft.VTail.Weight, 'lbf' )
    print
    print 'Propulsion MOI :', AsUnit( Aircraft.Propulsion.MOI(), 'slug*ft**2' )
    print 'Wing       MOI :', AsUnit( Aircraft.Wing.MOI(), 'slug*ft**2' )
    print 'HTail      MOI :', AsUnit( Aircraft.HTail.MOI(), 'slug*ft**2' )
    print 'VTail      MOI :', AsUnit( Aircraft.VTail.MOI(), 'slug*ft**2' )
    print 'Aircraft   MOI :', AsUnit( Aircraft.MOI(), 'slug*ft**2' )
    print
    print 'HTail Length   : ', Aircraft.HTail.L
    print 'VTail Length   : ', Aircraft.VTail.L
    print
    print 'MainGear Base  :', Aircraft.MainGear.WheelBase()
    print 'NoseGear Base  :', Aircraft.NoseGear.WheelBase()
    OTANGLE = Aircraft.OverturnAngle()
    print 'Overturn Angle :', OTANGLE
    print
    print 'Aircraft   V_LO :', AsUnit( Aircraft.GetV_LO(), 'ft/s' )
    print 'Wing       V_LO :', AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s' )
    print 'Ground Roll Distance: ',  Aircraft.Groundroll()
    print 'LO Rate of Climb : ', AsUnit( Aircraft.Rate_of_Climb(Aircraft.GetV_LO()*1.07), 'ft/min' )
    print
    
    print 'LEHT to LEVT : ', Aircraft.HTail.LE(0*IN) - Aircraft.VTail.LE(0*IN)
    print 'TailTaperlength: ', Aircraft.Fuselage.TailTaper.FrontBulk.X[0]-Aircraft.HTail.LE(0*IN)

    H = max(Aircraft.Wing.Upper(0*IN), Aircraft.VTail.Tip()[2])
    W = Aircraft.Wing.b
    L = Aircraft.HTail.MaxTE()
    print
    print 'Wing Height    : ', Aircraft.Wing.Upper(0*IN)
    print 'Vertical Tail H: ', Aircraft.VTail.Tip()[2]
    print 'Width          : ', W
    print 'Length         : ', L
    print 'Sum of Lengths : ', AsUnit( (W + L + H), 'in' )

#    HTail.Draw2DAirfoilPolars(fig = 10)
#    Aircraft.Wing.Draw2DAirfoilPolars(fig = 9)
    
#    Aircraft.PlotCLCMComponents(fig = 8, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
#    Aircraft.PlotTailLoad(fig=7)
#    Aircraft.PlotTrimmedPolars(fig=6)
#    Aircraft.PlotCMPolars(5, (-10*ARCDEG, -2.5*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), (+0.5 * IN, -0.5 * IN))
#    Aircraft.PlotPolarsSlopes(fig=4)
#    Aircraft.WriteAVLAircraft('AVLAircraft.avl')
#    Aircraft.PlotDragBuildup(fig=3)
#    Aircraft.PlotVNDiagram(fig=2)
    Aircraft.Draw()
    pyl.show()
    
def profile_main():
    # This is the main function for profiling 
     # We've renamed our original main() above to real_main()
     import cProfile, pstats, StringIO
     prof = cProfile.Profile()
     prof = prof.runctx("real_main()", globals(), locals())
     stream = StringIO.StringIO()
     stats = pstats.Stats(prof, stream=stream)
     stats.sort_stats("time")  # Or cumulative
     stats.print_stats(80)  # 80 = how many to print
     # The rest is optional.
     # stats.print_callees()
     # stats.print_callers()
     print stream.getvalue()
     
if __name__ == '__main__':
    #main = profile_main
    main = real_main
    main()