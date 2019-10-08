from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, LBF, SLUG, FT, OZM, OZF
from scalar.units import AsUnit
from Aerothon.ACFuselage import ACFuselage
from Aerothon.DefaultMaterialsLibrary import Monokote
from Aircraft_Models.Reg2009Aircraft_RedBearon.Materials.Mats import ACTrussBH, ACTrussSkin, ACPlyBH, ACPlySkin, BassStringer, ACNoseComp

Fuselage = ACFuselage()
#
# Create the sections of the fuselage
#
Fuselage.AddSection('Nose'     , 4*IN,  1)
Fuselage.AddSection('PyldBay'  , 11*IN, 1)
Fuselage.AddSection('TailTaper')

#
# Size the engine fire wall
#
Fuselage.Nose.FrontBulk.Width    = 3*IN
Fuselage.Nose.FrontBulk.Height   = 4*IN
Fuselage.Nose.FrontBulk.Material = ACNoseComp
Fuselage.Nose.Align              = -1
Fuselage.Nose.SkinMat            = ACNoseComp

#
# Size the payload bay
#
Fuselage.PyldBay.FrontBulk.Width    = 6.5*IN
Fuselage.PyldBay.FrontBulk.Height   = 6*IN
Fuselage.PyldBay.BackBulk.Width     = 6.5*IN
Fuselage.PyldBay.BackBulk.Height    = 6*IN
Fuselage.PyldBay.FrontBulk.Material = ACNoseComp
Fuselage.PyldBay.BackBulk.Material  = ACTrussBH
Fuselage.PyldBay.SkinMat            = ACTrussSkin
# Actual section is missing top plate so ~75% of weight prediction and approx 60% of remaining material is NoseComposite
Fuselage.PyldBay.SkinMat.AreaDensity = ACTrussSkin.AreaDensity * 0.25 + ACNoseComp.AreaDensity * 0.6
Fuselage.PyldBay.StringerMat        = BassStringer

#
# Change the alignement of the tail taper section
#
Fuselage.TailTaper.BackBulk.Width  = 2.0*IN
Fuselage.TailTaper.BackBulk.Height = 2.0*IN
Fuselage.TailTaper.BackBulk.Material = ACTrussBH
Fuselage.TailTaper.BackBulk.X      = [40*IN,0*IN,0*IN]  #Just for viewing, will actually be placed by the HT in the Aircraft file
Fuselage.TailTaper.Align           = 1
Fuselage.TailTaper.SkinMat         = ACTrussSkin
Fuselage.TailTaper.StringerMat     = BassStringer

#
# Add some components to the nose section
#
Fuselage.TailTaper.AddComponent ("Battery"        , 3.5*OZF  , (0.25*IN,1.5*IN,1*IN)   , "Front"   , (0.2, 0.5, 0.35) )
Fuselage.Nose.AddComponent      ("FuelTank+Fuel"  , 6*OZF    , (2.5*IN,2*IN,1.25*IN)   , "Back"    , (0.75, 0.5, 0.7) )
Fuselage.Nose.AddComponent      ("NoseWheelServo" , 0.77*OZF , (.5*IN,1*IN,1*IN)       , "Bottom"  , (0.6 , 0.2, 0.0) )
Fuselage.Nose.AddComponent      ("EngineServo"    , 0.77*OZF , (.5*IN,1*IN,1*IN)       , "Right"   , (0.6 , 0.2, 0.5) )
Fuselage.TailTaper.AddComponent ("Receiver"       , 1.25*OZF , (.5*IN,1*IN,1*IN)       , "Front"   , (0.6 , 0.2, 0.5) )
Fuselage.PyldBay.AddComponent   ("WingBox"        , 0.3*LBF  , (-1.5*IN,6.5*IN,5.5*IN) ,  "Bottom" , (0.55,0.5,0)     )
Fuselage.PyldBay.AddComponent   ("RWingStrut"     , 0.15*LBF , (24*IN,0.25*IN,1.5*IN)  ,  "Bottom" , (0.35,0.0,0)     )
Fuselage.PyldBay.AddComponent   ("LWingStrut"     , 0.15*LBF , (24*IN,0.25*IN,1.5*IN)  ,  "Bottom" , (0.35,1.0,0)     )
#Fuselage.PyldBay.AddComponent   ("Payload"        , 23.0*LBF , (3*IN,4*IN,5*IN)        , "Bottom"  , (0.5 , 0.5, 0.5) )

#
# Define which section contains the CG of the aircraft
#
Fuselage.XcgSection = Fuselage.PyldBay
Fuselage.XcgSecFrac = 0.3

#
# Determine which bulkhead should be set by the horizontal tail
#
Fuselage.TailBulk = Fuselage.TailTaper.BackBulk

if __name__ == '__main__':
    import pylab as pyl
    
    Fuselage.Nose.Weight + Fuselage.Nose.FrontBulk.Weight + Fuselage.Nose.BackBulk.Weight
    
    print 'Composite Section:', Fuselage.Nose.Weight + Fuselage.Nose.FrontBulk.Weight + Fuselage.Nose.BackBulk.Weight
    print 'Nose      Length :', Fuselage.Nose.Length
    print 'PyldBay   Weight :', Fuselage.PyldBay.Weight
    print 'PyldBay   Length :', Fuselage.PyldBay.Length
    print 'TailTaper Weight :', Fuselage.TailTaper.Weight
    print 'TailTaper Length :', Fuselage.TailTaper.Length
    
    print 'Fuselage Weight    :', Fuselage.Weight
    print 'Fuselage MOI       :', AsUnit( Fuselage.MOI(), "slug*ft**2" )
    print 'Fuselage CG        :', AsUnit( Fuselage.CG(), "in" )
    print 'Fuselage Desired CG:', AsUnit( Fuselage.AircraftCG(), "in" )
    
    
    Fuselage.Draw()
    pyl.show()