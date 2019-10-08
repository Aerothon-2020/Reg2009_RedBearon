from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACPropeller import ACPropeller
from Aerothon.ACEngine import ACEngine
from Aerothon.ACPropulsion import ACPropulsion
import numpy as npy
from scalar.units import IN, LBF, PSFC, SEC, ARCDEG, FT, OZF, RPM, HP
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.D          = 14.5*IN
Prop.Thickness  = .5*IN
Prop.PitchAngle = 12*ARCDEG
Prop.dAlpha     = 0*ARCDEG
Prop.Solidity   = 0.0136
Prop.RD         = 3/8
Prop.AlphaStall = 14*ARCDEG
Prop.Weight     = 3/32*LBF

# Set Engine properties
Engine  = ACEngine()
Engine.Rbs          = 1.1
Engine.Rla          = 3.5
Engine.NumCyl       = 1
Engine.NumRev       = 1
Engine.CompRatio    = 9
Engine.Vd           = 0.607*IN**3
Engine.PistonSpeedR = 38.27*FT/SEC
Engine.MEPtlmt      = 10.1526*LBF/IN**2
Engine.SFCmt        = 1*PSFC
Engine.A_F          = 16
Engine.PS           = 1
Engine.LWH          = [4*IN, 2.5*IN, 4*IN]
Engine.Xat          = [0, 0.5, 0.5]
Engine.Weight       = 1.5*LBF

Engine.NoseCone.LenDi = [2*IN,1.125*IN]
Engine.Muffler.LenDi = [6*IN,1.5*IN]
Engine.DrawDetail   = True

#
# Curvefitting parameters
#
Engine.BMEPR        = 50.038*LBF/IN**2
Engine.Rnmt         = 0.01
Engine.Rtmt         = 1.5
Engine.Rnsfc        = 0.8


# Set Propulsion properties
Propulsion = ACPropulsion(Prop,Engine)
Propulsion.Alt  = 0*FT
Propulsion.Vmax = 100*FT/SEC
Propulsion.nV   = 20

if __name__ == '__main__':
    import pylab as pyl
    
    #
    # This data has been corrected for standard day
    #
    #            RPM,        Torque
    TestData = [(7000  *RPM, 107.35 *IN*OZF),
                (8500  *RPM, 104.24 *IN*OZF),
                (9500  *RPM, 101.13 *IN*OZF),
                (9700  *RPM, 98.02  *IN*OZF),
                (10600 *RPM, 102.69 *IN*OZF),
                (10800 *RPM, 98.02  *IN*OZF),
                (11000 *RPM, 101.13 *IN*OZF),
                (11200 *RPM, 99.57  *IN*OZF),
                (11600 *RPM, 98.02  *IN*OZF),
                (12900 *RPM, 93.35  *IN*OZF),
                (13300 *RPM, 91.79  *IN*OZF),
                (13600 *RPM, 91.79  *IN*OZF),
                (14600 *RPM, 88.68  *IN*OZF),
                (15600 *RPM, 79.35  *IN*OZF),
                (16300 *RPM, 77.76  *IN*OZF)]
    
    Engine.TestData = TestData
    Engine.PlotTestData()

    print "Static Thrust :", AsUnit( Propulsion.T(0*FT/SEC), "lbf")
    
    V = npy.linspace(0,100,30)*FT/SEC
    N = npy.linspace(1000,20000,30)*RPM
    Propulsion.PlotMatched(V, fig = 2)
    V2 = npy.linspace(0,100,5)*FT/SEC
    Propulsion.PlotTPvsN(N, V2, fig=3)
    
    Propulsion.Draw(fig=4)
    
    pyl.show()
    